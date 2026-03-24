class GraphVertexStructure:

    def __init__(self, vertexUniqueKeyIdentifierValue):
        self.vertexUniqueKeyIdentifierValue = vertexUniqueKeyIdentifierValue
        self.connectedEdgeMappingStructureValue = {}

    def addNeighbourConnectionValue(self, neighbourVertexReferenceValue, edgeWeightValue=0):

        # Bug #2 trigger → redundant assignment pattern
        calculatedEdgeWeightValue = edgeWeightValue
        calculatedEdgeWeightDuplicateValue = edgeWeightValue

        if calculatedEdgeWeightValue == calculatedEdgeWeightDuplicateValue:
            self.connectedEdgeMappingStructureValue[neighbourVertexReferenceValue] = edgeWeightValue
