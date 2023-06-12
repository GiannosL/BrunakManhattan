from source.view_models.gwas_vm import parse_snp_file, parse_gwas_file

class TestGuiFuncs:
    def test_parse_snp_file(self):
        filename: str = 'tests/snps_list.txt'
        snp_list: list[str] = parse_snp_file(snp_filename=filename)

        assert(snp_list.__len__() == 5)

    def test_parse_gwas_file(self):
        filename: str = 'tests/gwas_file.tsv'
        df = parse_gwas_file(gwas_filename=filename)
        print(df)

        assert(df.shape == (5,6))
