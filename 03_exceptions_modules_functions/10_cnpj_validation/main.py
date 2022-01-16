"""
51.010.555/0001-55
"""
from cnpj import validate, generate_cnpj

if __name__ == "__main__":
    for _ in range(100):
        cnpj = generate_cnpj(formated=True)
        valid = validate(cnpj)
        print(f"Is the CNPJ {cnpj} valid? {valid}")
