import os

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID


def create_searchable_data(root, indexdir="indexdir"):
    """Schema definition

    :param root:
    :param indexdir:
    :return:
    """
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT, textdata=TEXT(stored=True))

    if not os.path.exists(indexdir): os.mkdir(indexdir)

    # creating index writer to add doc as per schema
    ix = create_in(indexdir, schema)
    writer = ix.writer()

    fpaths = [os.path.join(root, i) for i in os.listdir(root)]
    for path in fpaths:
        try:
            fp = open(path, 'r')
            print("Path: ", path)
            text = fp.read()
            writer.add_document(title=path.split(os.path.sep)[1], path=path, content=text, textdata=text)
        except Exception as e:
            raise Exception(e)
        finally:
            fp.close()
    writer.commit()


if __name__ == "__main__":
    root = "corpus"
    create_searchable_data(root)
