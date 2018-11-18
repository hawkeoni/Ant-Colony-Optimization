import numpy as np
import xml.etree.ElementTree as ET

from binascii import hexlify, unhexlify


class CompleteGraph:

    def __init__(self, n=1, low=0, high=200, matrix=None):
        if matrix is not None:
            self._matrix = matrix
            self.nodes = matrix.shape[0]
        else:
            self.nodes = n
            self.randomize(low, high)
        np.fill_diagonal(self._matrix, 0)

    def randomize(self, low, high):
        shape = (self.nodes, self.nodes)
        self._matrix = np.random.randint(low, high, shape)
        np.fill_diagonal(self._matrix, 0)

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
        index = (max(index), min(index))
        return self._matrix[index]
