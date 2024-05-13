from src.markdown_include.markdown_include import markdown_include

def test():

    markdown_include('./tests/test.md')
    with open('./tests/test_mdincl_output.md', 'r') as output_file:
        output = output_file.read()
    with open('./tests/test_res.md', 'r') as expected_file:
        expected = expected_file.read()

    assert output == expected
