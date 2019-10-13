def plant_growing(years):

    if years == 1:
        return (0.8)
    else:
        return (plant_growing(years - 1)*1.5)
