try:
    from lxml import etree

    print("running with lxml.etree")
except:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")

        ditamap = etree.XML('''<?xml version="1.0"?>
        <!DOCTYPE map PUBLIC '-//OASIS//DTD DITA Map//EN' 'map.dtd'>
        <map>
            <title>Debrief Python Eclipse cheat sheets to DITA</title>
            <topicmeta>
                <searchtitle>Eclipse cheat sheets to PDF</searchtitle>
                <shortdesc>Document Publishing Adventures with the DITA Open Toolkit</shortdesc>
                <author>Debrief</author>
                <author>John Bampton</author>
                <source>http://debrief.info/</source>
                <publisher>Github John Bampton</publisher>
                <critdates>
                    <created date='s'/>
                </critdates>
                <audience type='programmer' job='troubleshooting' experiencelevel='expert'/>
                <category>Java</category>
                <category>Document Publishing</category>
                <othermeta name='Publishing' content='DITA'/>
            </topicmeta>

        </map>
        ''')


        # Write the XML to the output file
        with open('map.ditamap', 'w') as output_file:
            print(etree.tostring(ditamap))
            output_file.write(etree.tostring(ditamap))

    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")