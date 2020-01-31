def map_geometry_building_type(df):
    df['Geometry Building Type RECS'] = df['TYPEHUQ'].map({1: 'Mobile Home',
                                                           2: 'Single-Family Detached',
                                                           3: 'Single-Family Attached',
                                                           4: 'Multi-Family with 2 - 4 Units',
                                                           5: 'Multi-Family with 5+ Units'})
    return df


def map_geometry_house_size(df):
    df['TOTSQFT'] = df[['TOTHSQFT', 'TOTCSQFT']].max(axis=1)
    df.loc[:, 'Geometry House Size'] = 0
    df.loc[(df['TOTSQFT'] < 1500), 'Geometry House Size'] = '0-1499'
    df.loc[(df['TOTSQFT'] >= 1500) & (df['TOTSQFT'] < 2500),
           'Geometry House Size'] = '1500-2499'
    df.loc[(df['TOTSQFT'] >= 2500) & (df['TOTSQFT'] < 3500),
           'Geometry House Size'] = '2500-3499'
    df.loc[(df['TOTSQFT'] >= 3500), 'Geometry House Size'] = '3500+'
    return df


def map_bedrooms(df):
    df['Bedrooms'] = df['BEDROOMS'].map({0: 1,
                                         1: 1,
                                         2: 2,
                                         3: 3,
                                         4: 4,
                                         5: 5,
                                         6: 5,
                                         7: 5,
                                         8: 5,
                                         9: 5,
                                         10: 5})
    return df


def map_occupants(df):
    df['Occupants'] = df['NHSLDMEM'].map({1: 1,
                                          2: 2,
                                          3: 3,
                                          4: 4,
                                          5: 5,
                                          6: 6,
                                          7: 6,
                                          8: 6,
                                          9: 6,
                                          10: 6,
                                          11: 6,
                                          12: 6})
    return df


def map_geometry_wall_type(df):
    df['Geometry Wall Type'] = df['WALLTYPE'].map({1: 'Masonry',
                                                   2: 'WoodStud',
                                                   3: 'WoodStud',
                                                   4: 'Masonry',
                                                   5: 'WoodStud',
                                                   6: 'Masonry',
                                                   7: 'Masonry',
                                                   8: 'WoodStud',
                                                   9: 'WoodStud'})

    return df


def map_vintage(df):
    df['Vintage'] = df['YEARMADERANGE'].map({1: '<1950',
                                             2: '1950s',
                                             3: '1960s',
                                             4: '1970s',
                                             5: '1980s',
                                             6: '1990s',
                                             7: '2000s',
                                             8: '2000s'})

    return df


def map_location_region(df):
    df['Location Region'] = df['REPORTABLE_DOMAIN'].map({2: 'CR03',
                                                         3: 'CR03',
                                                         4: 'CR07',
                                                         5: 'CR07',
                                                         6: 'CR07',
                                                         7: 'CR04',
                                                         8: 'CR04',
                                                         9: 'CR04',
                                                         10: 'CR02',
                                                         11: 'CR02',
                                                         12: 'CR08',
                                                         13: 'CR08',
                                                         14: 'CR08',
                                                         15: 'CR08',
                                                         16: 'CR09',
                                                         17: 'CR09',
                                                         18: 'CR09',
                                                         19: 'CR09',
                                                         20: 'CR08',
                                                         21: 'CR09',
                                                         22: 'CR09',
                                                         23: 'CR05',
                                                         24: 'CR05',
                                                         25: 'CR10',
                                                         26: 'CR10',
                                                         27: 'CR11',
                                                         })
    # Split out Kentucky and put in 8:
    df.loc[(df['REPORTABLE_DOMAIN'] == 18) & (
        df['AIA_Zone'] == 3), ['Location Region']] = 'CR08'

    return df
