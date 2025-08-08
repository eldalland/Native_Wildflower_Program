class WildFlower:
    def __init__(self, name, scientific, region, zone, safety, germination, info):
        self.name = name
        self.scientific = scientific
        self.region = region
        self.zone = zone
        self.safety = safety
        self.germination = germination
        self.info = info
        
                
        
    def return_name(self):
        return self.name 
    
    def set_name(self,name):
        self.name = name
    
    def return_scientific(self):
        return self.scientific 
    
    def set_scientific(self,scientific):
        self.scientific = scientific
    
    def return_region(self):
        return self.region
    
    def set_region(self,region):
        self.region = region
    
    def return_zone(self):
        return self.zone
    
    def set_zone(self,zone):
        self.zone = zone
    
    def return_safety(self):
        return self.safety
    
    def set_safety(self,safety):
        self.safety = safety
    
    def return_germination(self):
        return self.germination
    
    def set_germination(self,germination):
        self.germination = germination
    
    def return_germination_info(self):
        germination_str = ''
        for key, value in self.germination.items():
            germination_str += f'''
[green]{key}:[/green]
[purple]{value}[/purple]
                                   '''
        return germination_str
    
    def return_info(self):
        info_str = ''
        for key, value in self.info.items():
            info_str += f'''
[green]{key}:[/green]
[purple]{value}[/purple]
                                   '''
        return info_str
    
    def set_info(self,info):
        self.info = info