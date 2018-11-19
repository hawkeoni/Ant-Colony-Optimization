import argparse
import numpy as np
import xml.etree.ElementTree as ET

from binascii import hexlify, unhexlify


class CompleteGraph:

    def __init__(self, nodes=1, low=1, high=200, matrix=None):
        if matrix is not None:
            self._matrix = matrix
            self.nodes = matrix.shape[0]
        else:
            self.nodes = nodes
            self.randomize(low, high)

    def randomize(self, low, high):
        shape = (self.nodes, self.nodes)
        self._matrix = np.random.randint(low, high, shape)

    def to_xml(self, filename):
        xml_document = ET.Element('CompleteGraph')
        xml_document.attrib['nodes'] = str(self.nodes)
        for node in range(self.nodes - 1):
            line = hexlify(self._matrix[node][node:].tostring()).decode()
            sub_element = ET.SubElement(xml_document, "node_%d" % node)
            sub_element.text = line
        open(filename, 'w').write(ET.tostring(xml_document).decode())

    def from_xml(self, filename):
        tree = ET.ElementTree(file=filename)
        root = tree.getroot()
        self.nodes = int(root.attrib['nodes'])
        self._matrix = np.zeros((self.nodes, self.nodes))
        for node_num, node in enumerate(root):
            line = np.fromstring(unhexlify(node.text), dtype='int64')
            self._matrix[node_num][node_num:] = line

    def __getitem__(self, index):
        index = (min(index), max(index))
        return self._matrix[index]

class TSGraph(CompleteGraph):

    def __init__(self, nodes=1, phr=0.05, matrix=None, filename=None):
        if matrix is not None:
            CompleteGraph.__init__(matrix=matrix)
        elif filename is not None:
            CompleteGraph.__init__(self)
            self.from_xml(filename)
        else:
            CompleteGraph.__init__(self, nodes)
        self.pheromone = np.full((self.nodes, self.nodes), phr)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Graph generator')
    parser.add_argument('--size', type=int, default=5, help="Graph size")
    parser.add_argument('--file', type=str, default=None, help="Serialized graph filename")
    args = parser.parse_args()
    g = TSGraph(args.size)
    g.to_xml(args.file)