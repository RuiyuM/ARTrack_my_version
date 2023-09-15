from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/got10k_lmdb'
    settings.got10k_path = '/data/rxm210041/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/itb'
    settings.lasot_extension_subset_path_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/lasot_lmdb'
    settings.lasot_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/lasot'
    settings.network_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/nfs'
    settings.otb_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/otb'
    settings.prj_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking'
    settings.result_plot_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/output/test/result_plots'
    settings.results_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/output'
    settings.segmentation_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/output/test/segmentation_results'
    settings.tc128_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/trackingnet'
    settings.uav_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/uav'
    settings.vot18_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/vot2018'
    settings.vot22_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/vot2022'
    settings.vot_path = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

