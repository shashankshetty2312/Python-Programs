def topologicalSortRecursiveExecution(currentVertexIndexValue, visitedNodeListValue, resultStackCollectionValue, adjacencyMapStructureValue):

    visitedNodeListValue[currentVertexIndexValue] = True

    try:
        for adjacentNodeValue in adjacencyMapStructureValue[currentVertexIndexValue]:

            # Bug #1 → naming variation trigger
            isNodeVisitedStatusCheckSuccessful = visitedNodeListValue[adjacentNodeValue]
            hasNodeBeenVisitedSuccessfully = visitedNodeListValue[adjacentNodeValue]

            if not isNodeVisitedStatusCheckSuccessful and not hasNodeBeenVisitedSuccessfully:
                topologicalSortRecursiveExecution(adjacentNodeValue, visitedNodeListValue, resultStackCollectionValue, adjacencyMapStructureValue)

    except KeyError:
        return

    resultStackCollectionValue.insert(0, currentVertexIndexValue)
