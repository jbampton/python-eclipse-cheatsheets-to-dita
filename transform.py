import xml.etree.cElementTree as etree
print("running with cElementTree on Python 2.5+")

stylesheet="""<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:debrief="http://www.debrief.info/"
  exclude-result-prefixes="xs debrief"
  version="1.0">

  <xsl:template match="/compositeCheatsheet">
    <xsl:apply-templates select="taskGroup"/>
  </xsl:template>

  <xsl:template match="taskGroup">
    <task id="{generate-id(.)}">
      <title>
        <xsl:apply-templates select="@name"/>
      </title>
      <shortdesc>
        <xsl:apply-templates select="intro"/>
      </shortdesc>
      <xsl:choose>
        <xsl:when test="taskGroup">
          <xsl:apply-templates select="taskGroup"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:for-each select="task">
            <xsl:variable name="path" select="param[@name='path']/@value"/>
            <task id="{generate-id(.)}">
              <title>
                <xsl:apply-templates select="document($path)//cheatsheet/@title"/>
              </title>
              <shortdesc>
                <xsl:apply-templates select="document($path)//cheatsheet/intro/description"/>
              </shortdesc>
              <taskbody>
                <steps>
                  <xsl:apply-templates select="document($path)//cheatsheet"/>
                </steps>
                <result>
                  <xsl:apply-templates select="onCompletion"/>
                </result>
              </taskbody>
            </task>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>
    </task>
  </xsl:template>

  <xsl:template match="cheatsheet">
    <xsl:for-each select="item">
      <step id="{generate-id(.)}">
        <cmd>
          <xsl:apply-templates select="@title"/>
        </cmd>
        <info>
          <xsl:apply-templates select="description"/>
        </info>
        <stepxmp>
          <xsl:choose>
            <xsl:when test="@skip = 'true'">optional</xsl:when>
          </xsl:choose>
        </stepxmp>
      </step>
    </xsl:for-each>
  </xsl:template>

  <xsl:template match="b">
   <b><xsl:apply-templates/></b>
  </xsl:template>

  <xsl:template match="text()">
    <xsl:copy/>
  </xsl:template>

  <xsl:template match="i[.= 'NoPrint']"/>

  <xsl:template match="text()[preceding-sibling::i[.='NoPrint'][1]][following-sibling::i[.='NoPrint'][1] ] | *[preceding-sibling::i[.='NoPrint'][1]][following-sibling::i[.='NoPrint'][1] ]"/>

  <xsl:template match="br">
    <ph></ph>
  </xsl:template>

  <xsl:template match="i">
    <xsl:apply-templates/>
  </xsl:template>

</xsl:stylesheet>"""





ditamap = etree.XML('''<?xml version="1.0"?>
<!DOCTYPE map PUBLIC '-//OASIS//DTD DITA Map//EN' 'map.dtd'>
<map>
    <title>Debrief Python Eclipse cheat sheets to DITA</title>
    <topicmeta>
        <searchtitle>Eclipse cheat sheets to PDF</searchtitle>
        <shortdesc>Document Publishing Adventures with Python</shortdesc>
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
with open('output/map.ditamap', 'w') as output_file:
    print(etree.tostring(ditamap))
    output_file.write(etree.tostring(ditamap))