import pandas as pd

class Cleaner:
    COLS = ['Valeur fonciere', 'Nature mutation', 'Type local', 'Code departement', 'Date mutation', "No voie", "Code voie", "Code postal", "Commune", "Code commune", "Surface reelle bati"]

    def __init__(self):
        pass

    def load(self, files: list[str]) -> pd.DataFrame:
        self.df = pd.concat([pd.read_csv(file, sep='|', decimal=',', usecols=self.COLS) for file in files])

    def clean(self):
        self.df['Nature mutation'] = self.df['Nature mutation'].astype('category')