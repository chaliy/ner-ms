from ner import extract, extract_from_text, info

def test_info():
    res = info()
    assert res is not None

def test_extract():
    res = extract({
        'tokens': [
            'Несе',
            'Галя',
            'воду',
            ',',
            'Коромисло',
            'гнеться',
            ',',
            'За',
            'нею',
            'Іванко',
            ',',
            'Як',
            'барвінок',
            ',',
            'в',
            '`ється',
            '.'
         ]
    })
    assert res.get('entities') is not None
    assert res.get('entities')[0].get('label') is 'Галя'
    assert res.get('entities')[1].get('label') is 'Іванко'

def test_extract_empty_tokens():
    res = extract({
        'tokens': []
    })
    assert res.get('entities') is not None
