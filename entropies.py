#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maksim
@author: yuriy
"""

import os
import re
import numpy as np
import antropy as ant
import EntropyHub as EH
from NNetEn import NNetEn_entropy
from datetime import datetime
from tqdm import tqdm

config_entropy = {
    'svd_order': 9,
    'svd_delay': 1,
    'perm_order': 3,
    'perm_delay': 1,
    'app_dim': 2,
    'app_r': 0.2,
    'sampl_dim': 2,
    'sampl_r': 0.2,
    'bub_dim': 2,
    'cosi_dim': 2,
    'cosi_r': 0.1,
    'dist_dim': 2,
    'fuzz_dim': 1,
    'fuzz_r1': 0.01,
    'fuzz_r2': 1,
    'phase_k': 4,
    'nneten_ds': 'D1',
    'nneten_mu': 1,
    'nneten_method': 3,
    'nneten_metric': 'Acc',
    'nneten_epoch': 5
}

base_config = {
    'params': 1,
    'entropy_params': config_entropy,
    'input_file': os.path.join(os.path.dirname(__file__), '10sec_A3_small.txt')
}

names_entropy = ('SVD', 'Perm', 'ApEn', 'SampEn', 'BubbEn', 'CoSiEn',
                 'DistEn', 'FuzzEn', 'PhasEn', 'NNetEn')


def read_file_time_series(input_file: str) -> list:
    result = []
    with open(input_file) as file:
        line_list = file.readlines()
        for lines in line_list:
            lines = re.sub(r'[^(0-9.,\-eE \t)]', '', lines.strip())
            lines = lines.replace(',', '.')
            lines = re.sub(r'[ \t]+', ' ', lines, 0)
            if lines != '':
                result.append(lines.split(' '))

    return [np.array(data).astype(float) for data in result]


def calculate_entropy(params: int, data: list, config: dict) -> list:
    result = []
    progress_bar_params = {'ascii': True, 'desc': 'Series', 'ncols':60,
                           'bar_format': "{desc} :{percentage:3.0f}% |{bar}| {n_fmt}/{total_fmt}"}
    if params == 1:
        for series in tqdm(data, **progress_bar_params):
            result.append(ant.svd_entropy(series, order=config['svd_order'],
                                          delay=config['svd_delay'], normalize=True))
    elif params == 2:
        for series in tqdm(data, **progress_bar_params):
            result.append(ant.perm_entropy(series, order=config['perm_order'],
                                           delay=config['perm_delay'], normalize=True))
    elif params == 3:
        for series in tqdm(data, **progress_bar_params):
            app_ent, _ = EH.ApEn(series, m=config['app_dim'],
                                 r=config['app_r'] * np.std(series, ddof=0))
            result.append(app_ent[-1])
    elif params == 4:
        for series in tqdm(data, **progress_bar_params):
            samp_ent, _, _ = EH.SampEn(series, m=config['sampl_dim'],
                                       r=config['sampl_r'] * np.std(series, ddof=0))
            result.append(samp_ent[-1])
    elif params == 5:
        for series in tqdm(data, **progress_bar_params):
            bubb, renyi = EH.BubbEn(series, m=config['bub_dim'])
            result.append(bubb[-1])
    elif params == 6:
        for series in tqdm(data, **progress_bar_params):
            CoSiEn, _ = EH.CoSiEn(series, m=config['cosi_dim'], r=config['cosi_r'])
            result.append(CoSiEn)
    elif params == 7:
        for series in tqdm(data, **progress_bar_params):
            DistEn, _ = EH.DistEn(series, m=config['dist_dim'], Bins='sqrt')
            result.append(DistEn)
    elif params == 8:
        for series in tqdm(data, **progress_bar_params):
            FuzzEn, _, _ = EH.FuzzEn(series, m=config['fuzz_dim'],
                                     r=(config['fuzz_r1'] * np.std(series), config['fuzz_r2']))
            result.append(FuzzEn[-1])
    elif params == 9:
        for series in tqdm(data, **progress_bar_params):
            result.append(EH.PhasEn(series, K=config['phase_k']))
    elif params == 10:
        NNetEn = NNetEn_entropy(database=config['nneten_ds'], mu=config['nneten_mu'])
        for series in tqdm(data, **progress_bar_params):
            result.append(NNetEn.calculation(series, epoch=config['nneten_epoch'],
                                             method=config['nneten_method'],
                                             metric=config['nneten_metric'], log=False))

    return result


def run_calculate_entropy(config_dict):
    if os.path.isfile(config_dict['input_file']) and 1 <= config_dict['params'] <= 10:
        print('Start calculation entropy - {}'.format(names_entropy[config_dict['params'] - 1]))
        data = read_file_time_series(config_dict['input_file'])

        print('Read {} episodes from the file - {}'.format(len(data), config_dict['input_file']))
        res = calculate_entropy(config_dict['params'], data, config_dict['entropy_params'])

        out_file_name = '{}_result_{}_entropy_file_{}.txt'.format(
            datetime.now().strftime("%Y%m%d_%H%M%S"), names_entropy[config_dict['params'] - 1],
            os.path.basename(config_dict['input_file']).split('.')[0])
        np.savetxt(out_file_name, res, fmt='%g')

        print('Done calculation. Result write to file - {}'.format(out_file_name))
    else:
        print('Check the data file name and the parameter must be between 1 and 10')


def main():
    run_calculate_entropy(config_dict=base_config)


if __name__ == '__main__':
    main()
