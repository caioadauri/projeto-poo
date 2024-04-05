import pandas as pd

class Read():

  def __init__(self, file, sheet_name, usecols, skiprows, nrows, engine):
    self.file = file
    self.sheet_name = sheet_name
    self.usecols = usecols
    self.skiprows = skiprows
    self.nrows = nrows
    self.engine = engine
    self.dataframe = pd.read_excel(file, sheet_name, usecols=usecols, skiprows=skiprows, nrows=nrows, engine=engine)