class ModelBaseConfig():
    def __init__(self):
        pass
    
    # Path parameters
    data_path = 'data/corpora/BEST'
    log_path = 'tf_logs'

    # Training parameters
    verbose = 2
    batch_size = 512
    epochs = 20

    # Model parameters
    input_dim = 21
    output_dim = 1
    
class FFNNDOConfig(ModelBaseConfig):
    def __init__(self):
        super().__init__()
        
    # Training parameters
    batch_size = 1024
    
    # Model parameters
    dropout = 0.5
