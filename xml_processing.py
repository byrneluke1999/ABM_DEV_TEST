# # #
# I made use of the ElementTree XML API to solve this problem. Reading in the xml storing it as a hierarchical structure.
# Then simply calling the .find method on the root of this structure to find the RefText with the appropriate RefCode.
# I thought about what to do if a RefCode didn't exist and after some deliberation I opted for a try/except construction to
# catch any exceptions that might occur in retrieval (I didn't specify for generality), returning "N\A" for the unavailable codes.
# Some tests are included in the main.
# # #

import xml.etree.ElementTree as ET
xmlFile = "inputDoc.xml"


def extractReftextVals(RCode):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    try:
        for child in root.find(".//DeclarationHeader/Reference[@RefCode='{}']".format(RCode)):
            return child.text
    except:
        return "N/A"


def main():
    # TEST ONE - true
    RefCode = "MWB"
    print("The RefText value for code " + RefCode +
          " is " + extractReftextVals(RefCode))

    # TEST TWO - true
    RefCode = "TRV"
    print("The RefText value for code " + RefCode +
          " is " + extractReftextVals(RefCode))

    # TEST THREE - true
    RefCode = "CAR"
    print("The RefText value for code " + RefCode +
          " is " + extractReftextVals(RefCode))

    # TEST FOUR - false
    RefCode = "LOL"
    print("The RefText value for code " + RefCode +
          " is " + extractReftextVals(RefCode))


if __name__ == "__main__":
    main()
