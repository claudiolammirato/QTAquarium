import toml


class ConfigClass():
    def __init__(self):
        super().__init__()
    
    def load_item(self, filename):
        # Load a TOML file
        with open(''+filename+'.toml', 'r') as f:
            config = toml.load(f)
            return config
        
    def save_item(self, filename,cluster, item, value):
        # Load a TOML file
        with open(''+filename+'.toml', 'r') as f:
            config = toml.load(f)
            
        # Modify values in the config
        config[cluster][item] = value
 
        # Write the modified config back to the file
        with open(''+filename+'.toml', 'w') as f:
            toml.dump(config, f)


 
