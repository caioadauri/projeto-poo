class Convert():
  def __init__(self, dataframe, name_file):
    self.dataframe = dataframe
    self.name_file = name_file
    self.dataframe.to_csv(name_file, index=False)