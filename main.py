def main_function(geo_args, phys_args):
    background_grid = do_setup()
    phase_grid = geometry.identify_phases(background_grid, geo_args)
    fields = math.create_fields(background_grid, phase_grid, phys_args)
    ds = yt_section.convert_to_dataset(fields)
    return ds

#geometry section 
#code leader: Parsa
def identify_phases():
    pass

#math section 
#code leader: Jewon
def create_fields():
    pass

#yt section 
#code leader: Vayun
def convert_to_dataset():
    pass
