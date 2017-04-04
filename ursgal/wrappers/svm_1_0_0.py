#!/usr/bin/env python3.4
import ursgal
import os


class svm_1_0_0( ursgal.UNode ):
    """svm_1_0_0 UNode"""

    META_INFO = {
        'edit_version'      : 1.00,                                             # flot, inclease number if something is changed (kaz)
        'name'              : 'Svm',                                            # str, Software name (kaz)
        'version'           : '1.0.0',                                          # str, Software version name (kaz)
        'release_date'      : None,                                             # None, '%Y-%m-%d' or '%Y-%m-%d %H:%M:%S' (kaz)
        'engine_type' : {
            'validation_engine' : True,
        },
        'input_extensions'  : ['.csv'],                                         # list, extensions (kaz)
        'input_multi_file'  : False,                                            # bool, fill true up if multiple files input is MUST like venn-diagram (kaz)
        'output_extensions' : ['.csv'],                                         # list, extensions (kaz)
        'output_suffix'     : 'svm_validated',
        'create_own_folder' : False,
        'in_development'    : True,  # do not show in UNode overview
        'include_in_git'    : True,
        'engine' : {
            'platform_independent' : {
                'arc_independent' : {
                    'exe' : 'svm_1_0_0.py',
                },
            },
        },
    }

    def __init__(self, *args, **kwargs):
        super(svm_1_0_0, self).__init__(*args, **kwargs)

    def preflight(self):
        '''
        Building the list of parameters that will be passed to the
        svm_1_0_0 main function.

        These parameters are stored in self.params['command_list']

        Returns:
                None
        '''
        if not self.params['input_file'].lower().endswith('.csv'):
            raise ValueError(
                '\nSVM input file must be a unified CSV file, '
                'but you specified: ' + self.params['input_file']
            )

        in_path = os.path.join(
            self.params['input_dir_path'],
            self.params['input_file']
        )

        out_path = os.path.join(
            self.params['output_dir_path'],
            self.params['output_file']
        )

        self.params['command_list'] = [
            '/usr/bin/env',
            'python3',
            self.exe,
            '--input_csv',
            in_path,
            '--output_csv',
            out_path,
            '--kernel',
            self.params['kernel'],
            '--fdr_cutoff',
            str(self.params['fdr_cutoff']),
            '-c',
            str(self.params['translations']['svm_c_param']),
            #  '--mb_ram',
            #  str(self.params['available_RAM_in_MB']),
        ]

        if self.params.get('columns_as_features', False):
            self.params['command_list'].append(
                '--columns_as_features'
            )
            self.params['command_list'].append(
                ' '.join(self.params['columns_as_features'])
            )
        return

    def postflight(self):
        return
