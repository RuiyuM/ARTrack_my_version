class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/pretrained_networks'
        self.lasot_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/lasot'
        self.got10k_dir = '/data/rxm210041/got10k/train'
        self.got10k_val_dir = '/data/rxm210041/got10k/got10k/val'
        self.lasot_lmdb_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/got10k_lmdb'
        self.trackingnet_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/trackingnet_lmdb'
        self.coco_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/coco'
        self.coco_lmdb_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/vid'
        self.imagenet_lmdb_dir = '/home/012/r/rx/rxm210041/Desktop/ARTrack/tracking/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
