class FFNNConfig():
    def __init__(self):
        pass
    
    # Path parameters
    data_path = 'data/corpora/BEST'

    # Training parameters
    verbose = 1
    batch_size = 512
    epochs = 20

    # Model parameters
    input_dim = 21
    output_dim = 1