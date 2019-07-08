<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.2" tiledversion="1.2.4" name="spritesheet_tiles" tilewidth="128" tileheight="128" spacing="2" tilecount="465" columns="31">
 <image source="spritesheet_tiles.png" width="4096" height="2048"/>
 <terraintypes>
  <terrain name="Grass" tile="69"/>
  <terrain name="dirt" tile="14"/>
  <terrain name="Sand" tile="68"/>
 </terraintypes>
 <tile id="0">
  <properties>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="wall_right" type="bool" value="true"/>
   <property name="well_left" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="6" terrain="1,1,2,2"/>
 <tile id="7" terrain="1,1,0,0"/>
 <tile id="14" terrain="1,1,1,1"/>
 <tile id="31">
  <properties>
   <property name="wall_left" type="bool" value="true"/>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="37" terrain="1,1,1,2"/>
 <tile id="38" terrain="1,1,1,0"/>
 <tile id="45" terrain="1,2,2,2"/>
 <tile id="62">
  <properties>
   <property name="wall_bottom" type="bool" value="true"/>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="68" terrain="2,2,2,2"/>
 <tile id="69" terrain="0,0,0,0"/>
 <tile id="76" terrain="1,1,2,2"/>
 <tile id="93">
  <properties>
   <property name="wall_left" type="bool" value="true"/>
   <property name="wall_right" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="99" terrain="2,1,1,1"/>
 <tile id="100" terrain="0,1,1,1"/>
 <tile id="107" terrain="2,1,2,2"/>
 <tile id="130" terrain="2,2,1,1"/>
 <tile id="131" terrain="0,0,1,1"/>
 <tile id="138" terrain="2,1,1,1"/>
 <tile id="155">
  <properties>
   <property name="wall_bottom" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="161" terrain="1,2,1,1"/>
 <tile id="162" terrain="1,0,1,1"/>
 <tile id="169" terrain="1,2,1,1"/>
 <tile id="192" terrain="1,2,2,2"/>
 <tile id="193" terrain="1,0,0,0"/>
 <tile id="200" terrain="1,2,1,2"/>
 <tile id="217">
  <properties>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="219">
  <objectgroup draworder="index">
   <object id="1" x="-5" y="-2" width="25" height="23"/>
   <object id="3" x="110" y="0" width="20" height="19"/>
   <object id="4" x="109" y="111" width="19" height="20"/>
   <object id="5" x="-4" y="107" width="24" height="19"/>
  </objectgroup>
 </tile>
 <tile id="220">
  <objectgroup draworder="index">
   <object id="2" x="109" y="0" width="20" height="129"/>
   <object id="3" x="-1" y="1" width="22" height="127"/>
  </objectgroup>
 </tile>
 <tile id="223" terrain="2,1,2,2"/>
 <tile id="224" terrain="0,1,0,0"/>
 <tile id="231" terrain="1,1,1,1"/>
 <tile id="254" terrain="2,1,2,1"/>
 <tile id="255" terrain="0,1,0,1"/>
 <tile id="262" terrain="2,1,2,1"/>
 <tile id="285" terrain="2,2,2,2"/>
 <tile id="286" terrain="0,0,0,0"/>
 <tile id="293" terrain="1,1,2,1"/>
 <tile id="316" terrain="1,2,1,2"/>
 <tile id="317" terrain="1,0,1,0"/>
 <tile id="324" terrain="1,1,1,2"/>
 <tile id="347" terrain="2,2,1,2"/>
 <tile id="348" terrain="0,0,1,0"/>
 <tile id="355" terrain="2,2,1,2"/>
 <tile id="372">
  <properties>
   <property name="wall_bottom" type="bool" value="true"/>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="378" terrain="2,2,2,1"/>
 <tile id="379" terrain="0,0,0,1"/>
 <tile id="403">
  <properties>
   <property name="wall_left" type="bool" value="true"/>
   <property name="wall_right" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="409" terrain="1,1,2,1"/>
 <tile id="416" terrain="2,2,1,1"/>
 <tile id="434">
  <properties>
   <property name="wall_bottom" type="bool" value="true"/>
   <property name="wall_top" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="440" terrain="1,1,0,1"/>
 <tile id="447" terrain="2,2,2,1"/>
</tileset>
