ursgal_params = {
    'batch_size' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "100000",
        'description' :  ''' sets the number of sequences loaded in as a batch from the database file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, sequence batch size',
        },
        'utag' : [
            'spectrum',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'cleavage_cterm_mass_change' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "17.00305",
        'description' :  ''' The mass added to the peptide C-terminus by protein cleavage ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, cleavage C-terminal mass change',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'cleavage_nterm_mass_change' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "1.00794",
        'description' :  ''' The mass added to the peptide N-terminus bz protein cleavage ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, cleavage N-terminal mass change',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compensate_small_fasta' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' compensate for very small database files. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'scoring, cyclic permutation',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_after_post_flight' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  ''' Compress after post flight: True or False to .GZ  NOTE: This is old stuff, init ? ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_ext_exculsion' : {
        'available_in_unode' : [
        ],
        'default_value' : [
            '.csv',
        ],
        'description' :  ''' file type excluded from compression ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_output' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  ''' Compress output: True or False to .GZ ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_raw_search_results_if_possible' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "True",
        'description' :  ''' Compress raw search result to .gz: True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'compress_raw_search_results_if_possible',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'cpus' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "multiprocessing.cpu_count() - 1",
        'description' :  ''' Number of used cpus/threads ''',
        'trigger_rerun' : False,
        'ukey_translation' : {
            'msgfplus_style_1' : '-thread',
            'myrimatch_style_1' : '-cpus <integer>',
            'omssa_style_1' : '-nt',
            'xtandem_style_1' : 'spectrum, threads',
        },
        'utag' : [
            'hardware_resources',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'csv_filter_rules' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' Rules are defined as list of tuples with the first tuple element as the column name/csv fieldname, the second tuple element the rule and the third tuple element the value which should be compared ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'database' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : None,
        'description' :  ''' Path to database file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-d',
            'myrimatch_style_1' : '-ProteinDatabase <string>',
            'omssa_style_1' : '-d',
        },
        'utag' : [
            'input',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'decoy_generation_mode' : {
        'available_in_unode' : [
        ],
        'default_value' : "shuffle_peptide",
        'description' :  ''' Decoy database: Creates a target decoy database based on shuffling of peptides or complete reversing the protein sequence (reverse_protein). ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'decoy_tag' : {
        'available_in_unode' : [
        ],
        'default_value' : "decoy_",
        'description' :  ''' decoy-specific tag to differentiate between targets and decoys ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'del_from_params_before_json_dump' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : [
            'grouped_psms',
        ],
        'description' :  ''' List of parameters that are deleted before .json is dumped (to not overload the .json with unimportant informations) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'del_from_params_before_json_dump',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'enzyme' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "trypsin",
        'description' :  ''' Enzyme: Rule of protein cleavage
            Possible cleavages are :
                'argc'           -> '[R]|{P}'
                'aspn'           -> '[X]|[D]'
                'aspn_gluc'
                'chymotrypsin'   -> '[FMWY]|{P}'
                'chymotrypsin_p' -> '[FMWY]|[X]'
                'cnbr'           -> '[M]|{P}'
                'elastase'       -> '[AGILV]|{P}'
                # Note not all search engines support all enzymes ! :)
                'formic_acid'    -> '[D]|{P}'
                'gluc'
                'lysc'
                'lysc_p'
                'lysn'
                'no_cleavage'
                'nonspecific'
                'pepsina'
                'semi_chymotrypsin'
                'semi_gluc'
                'semi_tryptic'
                'thermolysin_p'
                'top_down'
                'trypsin'
                'trypsin_chymotrypsin
                'trypsin_cnbr'
                'trypsin_p' ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'enzyme specificity',
            'msgfplus_style_1' : '-e',
            'myrimatch_style_1' : '-CleavageRules<str>',
            'omssa_style_1' : '-e',
            'xtandem_style_1' : 'protein, cleavage site',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
            'msgfplus_style_1' : {
                'alpha_lp' : '8',
                'argc' : '6',
                'aspn' : '7',
                'chymotrypsin' : '2',
                'glutamyl_endopeptidase' : '5',
                'lysc' : '3',
                'lysn' : '4',
                'no_cleavage' : '9',
                'nonspecific' : '0',
                'trypsin' : '1',
            },
            'omssa_style_1' : {
                'argc' : '1',
                'aspn' : '12',
                'aspn_gluc' : '14',
                'chymotrypsin' : '3',
                'chymotrypsin_p' : '18',
                'cnbr' : '2',
                'formic_acid' : '4',
                'gluc' : '13',
                'lysc' : '5',
                'lysc_p' : '6',
                'lysn' : '21',
                'no_cleavage' : '11',
                'nonspecific' : '17',
                'pepsina' : '7',
                'semi_chymotrypsin' : '23',
                'semi_gluc' : '24',
                'semi_tryptic' : '16',
                'thermolysin_p' : '22',
                'top_down' : '15',
                'trypsin' : '0',
                'trypsin_chymotrypsin' : '9',
                'trypsin_cnbr' : '8',
                'trypsin_p' : '10',
            },
            'xtandem_style_1' : {
                'argc' : '[R]|{P}',
                'aspn' : '[X]|[D]',
                'chymotrypsin' : '[FMWY]|{P}',
                'chymotrypsin_p' : '[FMWY]|[X]',
                'clostripain' : '[R]|[X]',
                'cnbr' : '[M]|{P}',
                'elastase' : '[AGILV]|{P}',
                'formic_acid' : '[D]|{P}',
                'gluc' : '[DE]|{P}',
                'gluc_bicarb' : '[E]|{P}',
                'iodosobenzoate' : '[W]|[X]',
                'lysc' : '[K]|{P}',
                'lysc_p' : '[K]|[X]',
                'lysn' : '[X]|[K]',
                'lysn_promisc' : '[X]|[AKRS]',
                'nonspecific' : '[X]|[X]',
                'pepsina' : '[FL]|[X]',
                'protein_endopeptidase' : '[P]|[X]',
                'staph_protease' : '[E]|[X]',
                'tca' : '[FMWY]|{P},[KR]|{P},[X]|[D]',
                'trypsin' : '[KR]|{P}',
                'trypsin_cnbr' : '[KR]|{P},[M]|{P}',
                'trypsin_gluc' : '[DEKR]|{P}',
                'trypsin_p' : '[RK]|[X]',
            },
        },
        'uvalue_type' : [
            'argc',
            'aspn',
            'aspn_gluc',
            'chymotrypsin',
            'chymotrypsin_p',
            'cnbr',
            'elastase',
            'formic_acid',
            'gluc',
            'lysc',
            'lysc_p',
            'lysn',
            'no_cleavage',
            'nonspecific',
            'pepsina',
            'semi_chymotrypsin',
            'semi_gluc',
            'semi_tryptic',
            'thermolysin_p',
            'top_down',
            'trypsin',
            'trypsin_chymotrypsin',
            'trypsin_cnbr',
            'trypsin_p',
        ],
    },
    'filter_csv_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "filter_csv_1_0_0",
        'description' :  ''' filter csv converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'filter_csv_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'forbidden_cterm_mods' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "[]",
        'description' :  ''' List of modifications (unimod name) that are not allowed to occur at the C-terminus of a peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'residue, potential modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'force' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' If set 'True', engines are forced to re-run although no node-related parameters have changed ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'force',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'frag_mass_tolerance' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "monoisotopic",
        'description' :  ''' Fragment mass type: monoisotopic or average ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-to',
            'xtandem_style_1' : 'spectrum, fragment monoisotopic mass error',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'frag_mass_tolerance_unit' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "ppm",
        'description' :  ''' Fragment mass tolerance unit: available in ppm (parts-per-millon), Da (Dalton) or mmu (Milli mass unit) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, fragment monoisotopic mass error units',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'frag_mass_type' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "monoisotopic",
        'description' :  ''' Fragment mass type: monoisotopic or average ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-tom',
            'xtandem_style_1' : 'spectrum, fragment mass type',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'frag_method' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
        ],
        'default_value' : "hcd",
        'description' :  ''' used fragmentation method. e.g. collision-induced dissociation (CID), electron-capture dissociation (ECD), electron-transfer dissociation (ETD), Higher-energy C-trap dissociation (HCD) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-m',
            'myrimatch_style_1' : '-FragmentationRule<str>',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
            'msgfplus_style_1' : {
                'cid' : '1',
                'etd' : '2',
                'hcd' : '3',
            },
        },
        'uvalue_type' : [
            'cid',
            'ecd',
            'etd',
            'hcd',
        ],
    },
    'frag_min_mz' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "150",
        'description' :  ''' minimal considered fragment ion m/z ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, minimum fragment mz',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ftp_blocksize' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : 1024,
        'description' :  ''' Blocksize for ftp download ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_blocksize',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_folder' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp folder that should be downloaded ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_include_ext' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Only files with the defined file extension are downloaded with ftp download ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_include_ext',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_max_number_of_files' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Maximum number of files that will be downloaded ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_max_number_of_files',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_output_folder' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Default ftp download path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_output_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_password' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp download password ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_password',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_url' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp download URL, will fail if it is not set by the user ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_url',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'helper_extension' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".u.json",
        'description' :  ''' Exension for helper files ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'helper_extension',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'http_output_folder' : {
        'available_in_unode' : [
            'get_http_files_1_0_0',
        ],
        'default_value' : "None",
        'description' :  ''' Default http download path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'http_output_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'http_url' : {
        'available_in_unode' : [
            'get_http_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' http download URL, will fail if it is not set by the user ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'http_url',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'include_reverse (not used)' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  ''' A target decoy database should be generated independently from the search engine, e.g. by using the uNode generate_target_decoy ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'generate_decoy',
            'msgfplus_style_1' : '-tda',
            'xtandem_style_1' : 'scoring, include reverse',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'input_file' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  ''' Input file: path/to/input/file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-s',
            'xtandem_style_1' : 'spectrum, path',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'input_file_type' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "None",
        'description' :  ''' Input file type ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, path type',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'java_-Xmx' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : "13312m",
        'description' :  ''' Set maximum Java heap size (used RAM) ''',
        'trigger_rerun' : False,
        'ukey_translation' : {
            'msgfplus_style_1' : '-Xmx',
        },
        'utag' : [
            'hardware_resources',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'json_extension' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".u.json",
        'description' :  ''' Exension for .json files ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'json_extension',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'label' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "14N",
        'description' :  ''' 15N if the corresponding amino acid labeling was applied ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-tem / -tom',
            'xtandem_style_1' : 'protein, modified residue mass file',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'log_enabled' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Will redirect sys.stdout to the logfile, default name: ursgal.log ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'log_enabled',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'log_file_name' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "None",
        'description' :  ''' This can be used to specify a different log file path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'log_file_name',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'machine_offset_in_ppm' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' Machine offset ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'max_mod_alternatives' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "6",
        'description' :  ''' Maximal number of variable modification alternatives, given as C in 2^C ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, ptm complexity',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'max_num_mods' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : "2",
        'description' :  ''' Maximal number of modifications per peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : 'NumMods',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'max_num_per_mod' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "{}",
        'description' :  ''' Maximal number of modification sites per peptide for a specific modification, given as a dictionary: {unimod_name : number} ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'residue, potential modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'max_pep_length' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : "40",
        'description' :  ''' Maximal length of a peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-maxLength',
            'myrimatch_style_1' : '-MaxPeptideLength<int>',
            'omssa_style_1' : '-nox',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'maximal_accounted_observed_peaks' : {
        'available_in_unode' : [
            'myrimatch',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "50",
        'description' :  ''' Maximum number of peaks from a spectrum used. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : '-MaxPeakCount',
            'xtandem_style_1' : 'spectrum, total peaks',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'maximum_missed_cleavages' : {
        'available_in_unode' : [
            'msamanda',
            'myrimatch',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "2",
        'description' :  ''' Maximum number of missed cleavages per peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'missed_cleavages',
            'myrimatch_style_1' : '-MaxMissedCleavages<int>',
            'xtandem_style_1' : 'scoring, maximum missed cleavage sites',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'maximum_pep_for_ident_csv' : {
        'available_in_unode' : [
        ],
        'default_value' : "0.1",
        'description' :  ''' Maximum value for PEP (posterior error probability): Threshold for identifications put in CSV-files. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'mgf_input_file' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : None,
        'description' :  ''' Path to input .mgf file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-s',
        },
        'utag' : [
            'input',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'min_pep_length' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : "6",
        'description' :  ''' Minimal length of a peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-minLength',
            'myrimatch_style_1' : '-MinPeptideLength<int>',
            'omssa_style_1' : '-no',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'mininimal_required_matched_peaks' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "4",
        'description' :  ''' Mimimum number of matched ions required for a peptide to be scored ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-hm',
            'xtandem_style_1' : 'scoring, minimum ion count',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'mininimal_required_observed_peaks' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "5",
        'description' :  ''' Mimimum number of peaks in the spectrum to be considered. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-hs',
            'xtandem_style_1' : 'spectrum, minimum peaks',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'modifications' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : [
            '*,opt,Prot-N-term,Acetyl',
            'M,opt,any,Oxidation',
        ],
        'description' :  ''' Modifications are given as a list of strings, each representing the modification of one amino acid. The string consists of four informations seperated by comma:

'amino acid,type,position,unimod name’

 amino acid : specify the modified amino acid as a single letter, use '*' if the amino acid is variable

 type   : specify if it is a fixed (fix) or potential (opt) modification

 position  : specify the position within the protein/peptide (Prot-N-term, Prot-C-term), use 'any' if the positon is variable

 unimod name : specify the unimod PSI-MS Name (see unimod.org)

Examples:

 [ 'M,opt,any,Oxidation' ]   - potential oxidation of Met at any position within a peptide

 [ '*,opt,Prot-N-term,Acetyl' ]  - potential acetylation of any amino acid at the N-terminus of a protein

 [ 'S,opt,any,Phospho' ]   - potential phosphorylation of Serine at any position within a peptide

 ['C,fix,any,Carbamidomethyl’, 'N,opt,any,Deamidated’, 'Q,opt,any,Deamidated’] - fixed carbamidomethylation of Cys and potential deamidation of Asn and/or Gln at any position within a peptide

Additionally, userdefined modifications can be given and are written to a userdefined_unimod.xml in ursgal/kb/ext. Userdefined modifications need to have a unique name instead of the unimod name the chemical composition needs to be given as a Hill notation on the fifth position in the string

Example:

 [ 'S,opt,any,New_mod,C2H5N1O3' ] ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'modification protein=true cterm=true',
            'msgfplus_style_1' : '-mod',
            'myrimatch_style_1' : '-StaticMods<str>',
            'omssa_style_1' : '-mv',
            'xtandem_style_1' : 'protein, C-terminal residue modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'msgfplus_protocol_id' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : 0,
        'description' :  ''' MS-GF+ specific protocol identifier. Protocols are used to enable scoring parameters for enriched and/or labeled samples. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-protocol',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            '0',
            '1',
            '2',
            '3',
        ],
    },
    'mzidentml_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "mzidentml_lib_1_6_10",
        'description' :  ''' mzidentml converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'mzidentml_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'mzml2mgf_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "mzml2mgf_1_0_0",
        'description' :  ''' mzml to mgf converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'mzml2mgf_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'neutral_loss_enabled' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Neutral losses enabled for spectrum algorithm: set  True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, use neutral loss window',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'neutral_loss_mass' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "0",
        'description' :  ''' Sets the centre of the window for ignoring neutral molecule losses. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, neutral loss mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'neutral_loss_window' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "0",
        'description' :  ''' Neutral loss window: sets the width of the window for ignoring neutral molecule losses. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, neutral loss window',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'noise_suppression_enabled' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' used for noise suppresssion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, use noise suppression',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'num_match_spec' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : 10,
        'description' :  ''' This parameter sets the maximum number of peptide spectrum matches to report for each spectrum ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'Specify the number of matches to report for each spectrum',
            'msgfplus_style_1' : '-n',
            'myrimatch_style_1' : 'This parameter sets the maximum rank of peptide-spectrum-matches to report for each spectrum',
            'omssa_style_1' : 'maximum number of hits retained per precursor charge state per spectrum',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'number_of_i_decimals' : {
        'available_in_unode' : [
        ],
        'default_value' : "5",
        'description' :  ''' Number of decimals for intensity (peak) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'number_of_mz_decimals' : {
        'available_in_unode' : [
        ],
        'default_value' : "5",
        'description' :  ''' Number of decimals for m/z mass ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'output_file_incl_path' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : None,
        'description' :  ''' Path to output file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-o',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'output_file_type' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' Output file type ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'output_suffix' : {
        'available_in_unode' : [
        ],
        'default_value' : "",
        'description' :  ''' Output suffix: string ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_isotope_range' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "0,1",
        'description' :  ''' Error range for incorrect carbon isotope parent ion assignment ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-ti',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass isotope error',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                '0' : 'no',
                '0,1' : 'yes',
                '0,2' : 'yes',
            },
        },
        'uvalue_type' : [
            '0',
            '0,1',
            '0,2',
        ],
    },
    'precursor_mass_tolerance_minus' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 5,
        'description' :  ''' Precursor mass tolerance: lower mass tolerance of measured and calculated parent ion M+H ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol',
            'msgfplus_style_1' : '-t',
            'myrimatch_style_1' : '-MonoPrecursorMzTolerance',
            'omssa_style_1' : '-te',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error minus',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_mass_tolerance_plus' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "5",
        'description' :  ''' Precursor mass tolerance: higher mass tolerance of measured and calculated parent ion M+H ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol',
            'omssa_style_1' : '-te',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error plus',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_mass_tolerance_unit' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "ppm",
        'description' :  ''' Precursor mass tolerance unit: available in ppm (parts-per-millon), da (Dalton) or mmu (Milli mass unit) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol unit',
            'msgfplus_style_1' : '-t',
            'omssa_style_1' : '-teppm',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error units',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            'da',
            'mmu',
            'ppm',
        ],
    },
    'precursor_mass_type' : {
        'available_in_unode' : [
            'msamanda',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : "monoisotopic, (average)",
        'description' :  ''' Precursor mass type: monoisotopic or average ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'monoisotopic',
            'myrimatch_style_1' : '-PrecursorMzToleranceRule <str>',
            'omssa_style_1' : '-tem',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                'average' : '1',
                'monoisotopic' : '0',
            },
        },
        'uvalue_type' : [
            'average',
            'monoisotopic',
        ],
    },
    'precursor_max_charge' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
        ],
        'default_value' : "5",
        'description' :  ''' maximal accepted parent ion charge ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'considered_charges',
            'msgfplus_style_1' : '-maxCharge',
            'myrimatch_style_1' : '-NumChargeStates <interger>',
            'omssa_style_1' : '-zh',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_min_charge' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'omssa_2_1_9',
        ],
        'default_value' : "1",
        'description' :  ''' minimal accepted parent ion charge ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'considered_charges',
            'msgfplus_style_1' : '-minCharge',
            'omssa_style_1' : '-zl',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_min_mass' : {
        'available_in_unode' : [
            'myrimatch',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "400",
        'description' :  ''' minimal parent ion mass ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : '-MinPeptideMass <real>',
            'xtandem_style_1' : 'spectrum, minimum parent m+h -sets the minimum parent M+H required for a spectrum to be considered.',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_ppm_offset' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : "None",
        'description' :  ''' Precursor offset in ppm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
            'mzml2mgf_style_1' : 'precursor_ppm_offset',
        },
        'uvalue_type' : "",
    },
    'prefix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "None",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'prefix',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'raw_ident_csv_suffix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".csv",
        'description' :  ''' CSV suffix of raw indentification: this is the conversion result after CSV conversion but before adding retention time ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'raw_ident_csv_suffix',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'remove_temporary_files' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Remove temporary files: True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'remove_temporary_files',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'rt_pickle_name' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "_ursgal_lookup.pkl",
        'description' :  ''' name of the pickle that is used to map the retention time ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'rt_pickle_name',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'scan_exclusion_list' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' spectra rejected during mzml2mgf conversion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'scan_skip_modulo_step' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' include only the n'th spectrum during mzml2mgf conversion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_-h2o_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, ions loss of H2O are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_-nh3_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, ions loss of NH3 are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_a_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, a ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, a ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_b_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "True",
        'description' :  ''' Spectrum: if true, b ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, b ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_c_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, c ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, c ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_imm_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, immonium ions are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_int_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, internal fragment ions are respect in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_x_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, x ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, x ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_y_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "True",
        'description' :  ''' Spectrum: if true, y ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, y ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_z+1_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, z ion plus 1 Da mass are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_z+2_ions' : {
        'available_in_unode' : [
            'msamanda',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true z ion plus 2 Da mass are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_z_ions' : {
        'available_in_unode' : [
            'msamanda',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Spectrum: if true, z ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, z ions',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'search_engines_create_folders' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "True",
        'description' :  ''' Create folders for search engines. True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'search_engines_create_folders',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'search_for_saps' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' search for potential single amino acid polymorphisms ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, saps',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'semi_enzyme' : {
        'available_in_unode' : [
            'msamanda',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Allows semi-enzymatic peptide ends ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'enzyme specificity',
            'msgfplus_style_1' : '-ntt',
            'myrimatch_style_1' : '-MinTerminiCleavages<int>',
            'xtandem_style_1' : 'protein, cleavage semi',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'show_unodes_in_development' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Show ursgal nodes that are in development: False or True ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'show_unodes_in_development',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'spec_dynamic_range' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "100",
        'description' :  ''' Spectrum, internal normalization: The highest peak (intensity) within a spectrum is set to given value and all other peaks are normalized to this peak. If the normalized value is less than 1 he peak is rejected. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, dynamic range',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'stp_bias' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' Interpretation of peptide phosphorylation models. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, stP bias',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey1' : {
        'available_in_unode' : [
            'msamanda',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'modification protein=true nterm=true',
            'xtandem_style_1' : 'protein, N-terminal residue modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey2' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, quick acetyl',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey3' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, quick pyrolidone',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey4' : {
        'available_in_unode' : [
            'msamanda',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'modification fix=true',
            'xtandem_style_1' : 'residue, modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey5' : {
        'available_in_unode' : [
            'msamanda',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'modification fix=false',
            'xtandem_style_1' : 'residue, potential modification mass',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'ukey6' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'residue, potential modification motif',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'unify_csv_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "unify_csv_1_0_0",
        'description' :  ''' unify csv converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'unify_csv_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'use_refine' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'validated_ident_csv_suffix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "validated.csv",
        'description' :  ''' CSV suffix of validated identification files: string, CSV-file which contains PSMs validated with validation tools ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'validated_ident_csv_suffix',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'validation_score_field' : {
        'available_in_unode' : [
            'percolator_2_08',
            'qvality_2_02',
        ],
        'default_value' : "",
        'description' :  ''' Name of the column that is used for validation, e.g. by qvality and percolator ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
            'percolator_style_1' : {
                'omssa_style_1' : 'OMSSA:pvalue',
            },
        },
        'uvalue_type' : "",
    },
    'write_unfiltered_results' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  ''' writes rejected results if True ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
}