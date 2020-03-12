# My approach was to split the EDIFACT message text into a list seperating each element by a new line (as it was supplied).
# Then looping through each element simply checking whether the string 'LOC' is a substring. In the case that it is, I split
# that string by the '+' symbol to extract the 1st, 2nd and 3rd elements of the segment.
# Then I simply populate the array with the 2nd and 3rd elements.
# NOTE
# I was unsure about what the populated array was to look like, initially just adding them to the array seemed fine. However,
# upon second thought I figured it made the most sense to group elements from the same segment together - Hence the tuple.
# # #


def findLOC(ediFile):
    ediLOC = []
    lines = ediFile.split("'\n")
    cSegment = []  # current segment
    for i in lines:
        if "LOC" in i:
            cSegment = i.split("+")
            # ediLOC.append(cSegment[1])
            # ediLOC.append(cSegment[2])
            ediLOC.append((cSegment[1], cSegment[2]))
    return ediLOC


def main():
    edi = """UNA: +.? &'
    UNB+UNOC: 3+2021000969+4441963198+180525: 1225+3VAL2MJV6EH9IX+KMSV7HMD+CUSDECU-IE++1++1&'
    UNH+EDIFACT+CUSDEC: D: 96B: UN: 145050&'
    BGM+ZEM:: : EX+09SEE7JPUV5HC06IC6+Z&'
    LOC+17+IT044100&'
    LOC+18+SOL&'
    LOC+35+SE&'
    LOC+36+TZ&'
    LOC+116+SE003033&'
    DTM+9: 20090527: 102&'
    DTM+268: 20090626: 102&'
    DTM+182: 20090527: 102&'"""
    print(findLOC(edi))


if __name__ == "__main__":
    main()
