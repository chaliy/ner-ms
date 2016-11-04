from ner import extract, info

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

def test_extract_nested():
    res = extract({
        'tokens': [[
            'Несе',
            'Галя',
            'воду',
        ],[
            'Коромисло',
            'гнеться',
        ], [
            'За',
            'нею',
            'Іванко',
        ], [
            'Як',
            'барвінок',
            ',',
            'в',
            '`ється',
        ]]
    })
    assert res.get('entities') is not None

def test_extract_statistics():
    res = extract({
        'tokens': [
            'Несе',
            'Галя',
            'воду'
         ]
    })
    assert res['statistics']['tokensCount'] is 3
    assert res['statistics']['entitiesCount'] is not 0

def test_extract_empty_tokens():
    res = extract({
        'tokens': []
    })
    assert res.get('entities') is not None

def test_extract_from_nothing():
    res = extract(None)
    assert len(res.get('entities')) is 0

def test_extract_from_almost_nothing():
    res = extract({})
    assert len(res.get('entities')) is 0
