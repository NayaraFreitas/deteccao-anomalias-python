import os
import pandas as pd



def load_credit_card_data():
    url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

    local_dir = os.path.join("data", "raw")
    local_path = os.path.join(local_dir, "creditcard.csv")

    if os.path.exists(local_path):
        print("Carregando dados localmente")
        df = pd.read_csv(local_path)


    else:
        print('Arquivo não encontrado')
        print("Baixando arquivo csv da internet , levará un momentinho")

        os.makedirs(local_dir, exist_ok=True)

        df= pd.read_csv(url)

        print('Salvando os dados na pasta data/raw')
        df.to_csv(local_path, index=False)

    print(f'Dataset pronto para uso {df.shape}')
    return df

if __name__ == "__main__":
    df_test = load_credit_card_data()
    