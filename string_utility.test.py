class StringUtil:
    @staticmethod
    def reverse_string(input_str):
        return input_str[::-1]

    @staticmethod
    def capitalize_string(input_str):
        return input_str.upper()

    @staticmethod
    def lowercase_string(input_str):
        return input_str.lower()


def test_reverse_string():
    # Given a string
    string = "aBc"
    
    # When the string is reversed
    result = StringUtil.reverse_string(string)
    
    # Then the result should be the reversed string
    assert result == "cBa"

def test_capitalize_string():
    # Given a string
    string = "aBc"
    
    # When the string is capitalized
    result = StringUtil.capitalize_string(string)
    
    # Then the result should be the capitalized string
    assert result == "ABC"

def test_lowercase_string():
    # Given a string
    string = "aBc"
    
    # When the string is lowercased
    result = StringUtil.lowercase_string(string)
    
    # Then the result should be the lowercased string
    assert result == "abc"

# Run the tests
if __name__ == "__main__":
    test_reverse_string()
    test_capitalize_string()
    test_lowercase_string()

    print("All tests passed!")
