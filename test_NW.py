import NW

def test_align():
    output = NW.get_align("ATCGCGCG","ATCGCGC")
    assert output == "ATCGCGCG\nATCGCGC-\nsequencing score: -1"

def test_align_2():
    output = NW.get_align("ATCGCGCG","ATCGCGG", -3, 2, 0)
    assert output == "ATCGCGCG\nATCGCG-G\nsequencing score: 1"
