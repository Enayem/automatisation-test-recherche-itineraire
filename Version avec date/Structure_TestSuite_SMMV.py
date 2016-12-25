########################################################################################
#                                                                                      #
#Programe de génération d'une "TestSuite SMMV"                                         #
#Fichier de structure                                                                  #
#Auteur : Omar ENAYEH 11/2016                                                          #
# IXXI                                                                                 #
########################################################################################


global HeadGlobal, BottomGlobal, testSuiteHead, testSuiteBottom, testStepHead, testStepBottom
HeadGlobal ="""<?xml version="1.0" encoding="UTF-8"?>
<con:soapui-project id="{uuid1}" activeEnvironment="Default" name="{projectName}" resourceRoot="" soapui-version="5.2.1" xmlns:con="http://eviware.com/soapui/config">
	<con:settings/>
	<con:interface xsi:type="con:WsdlInterface" id="{uuid2}" wsaVersion="NONE" name="SmartMoveServiceSoapBinding" type="wsdl" bindingName="http://smartmove.ixxi/SmartMoveServiceSoapBinding" soapVersion="1_2" anonymous="optional" definition="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		<con:settings/>
		<con:definitionCache type="TEXT" rootPart="">
			<con:part>
				<con:url></con:url>
				<con:content>
					<![CDATA[<wsdl:definitions name="SmartMoveService" targetNamespace="http://smartmove.ixxi/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:tns="http://smartmove.ixxi/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/">
  <wsdl:types>
    <xs:schema elementFormDefault="unqualified" targetNamespace="http://smartmove.ixxi/" version="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema">
      <xs:element name="affectScope" type="tns:affectScope"/>
      <xs:element name="affectedLine" type="tns:affectedLine"/>
      <xs:element name="callPoint" type="tns:callPoint"/>
      <xs:element name="city" type="tns:city"/>
      <xs:element name="direction" type="tns:direction"/>
      <xs:element name="ecoComparator" type="tns:ecoComparator"/>
      <xs:element name="getGroupOfLines" type="tns:getGroupOfLines"/>
      <xs:element name="getGroupOfLinesResponse" type="tns:getGroupOfLinesResponse"/>
      <xs:element name="getItinerary" type="tns:getItinerary"/>
      <xs:element name="getItineraryResponse" type="tns:getItineraryResponse"/>
      <xs:element name="getLineTimeTables" type="tns:getLineTimeTables"/>
      <xs:element name="getLineTimeTablesResponse" type="tns:getLineTimeTablesResponse"/>
      <xs:element name="getLines" type="tns:getLines"/>
      <xs:element name="getLinesResponse" type="tns:getLinesResponse"/>
      <xs:element name="getOperators" type="tns:getOperators"/>
      <xs:element name="getOperatorsResponse" type="tns:getOperatorsResponse"/>
      <xs:element name="getServicePatterns" type="tns:getServicePatterns"/>
      <xs:element name="getServicePatternsResponse" type="tns:getServicePatternsResponse"/>
      <xs:element name="getStatus" type="tns:getStatus"/>
      <xs:element name="getStatusResponse" type="tns:getStatusResponse"/>
      <xs:element name="getStopPlaces" type="tns:getStopPlaces"/>
      <xs:element name="getStopPlacesResponse" type="tns:getStopPlacesResponse"/>
      <xs:element name="getStopPoints" type="tns:getStopPoints"/>
      <xs:element name="getStopPointsResponse" type="tns:getStopPointsResponse"/>
      <xs:element name="getStops" type="tns:getStops"/>
      <xs:element name="getStopsResponse" type="tns:getStopsResponse"/>
      <xs:element name="groupOfLinesResultat" type="tns:groupOfLinesResultat"/>
      <xs:element name="infoMessage" type="tns:infoMessage"/>
      <xs:element name="itineraryResultat" type="tns:itineraryResultat"/>
      <xs:element name="line" type="tns:line"/>
      <xs:element name="lineJourney" type="tns:lineJourney"/>
      <xs:element name="lineTimeTable" type="tns:lineTimeTable"/>
      <xs:element name="lineTimeTablesResultat" type="tns:lineTimeTablesResultat"/>
      <xs:element name="linesResultat" type="tns:linesResultat"/>
      <xs:element name="notice" type="tns:notice"/>
      <xs:element name="objectId" type="tns:objectId"/>
      <xs:element name="operatorsResultat" type="tns:operatorsResultat"/>
      <xs:element name="pairDate" type="tns:pairDate"/>
      <xs:element name="pairIdName" type="tns:pairIdName"/>
      <xs:element name="resolveIds" type="tns:resolveIds"/>
      <xs:element name="resolveIdsResponse" type="tns:resolveIdsResponse"/>
      <xs:element name="resolveIdsResultat" type="tns:resolveIdsResultat"/>
      <xs:element name="riGeoPoint" type="tns:riGeoPoint"/>
      <xs:element name="riInput" type="tns:riInput"/>
      <xs:element name="riItinerary" type="tns:riItinerary"/>
      <xs:element name="searchGeoPoint" type="tns:searchGeoPoint"/>
      <xs:element name="segment" type="tns:segment"/>
      <xs:element name="serviceJourney" type="tns:serviceJourney"/>
      <xs:element name="servicePattern" type="tns:servicePattern"/>
      <xs:element name="servicePatternDetails" type="tns:servicePatternDetails"/>
      <xs:element name="servicePatternsResultat" type="tns:servicePatternsResultat"/>
      <xs:element name="setPerturbations" type="tns:setPerturbations"/>
      <xs:element name="setPerturbationsResponse" type="tns:setPerturbationsResponse"/>
      <xs:element name="situation" type="tns:situation"/>
      <xs:element name="stop" type="tns:stop"/>
      <xs:element name="stopPlace" type="tns:stopPlace"/>
      <xs:element name="stopPlacesResultat" type="tns:stopPlacesResultat"/>
      <xs:element name="stopPoint" type="tns:stopPoint"/>
      <xs:element name="stopPointsResultat" type="tns:stopPointsResultat"/>
      <xs:element name="stopsOnLine" type="tns:stopsOnLine"/>
      <xs:element name="stopsResultat" type="tns:stopsResultat"/>
      <xs:element name="trafficEventRef" type="tns:trafficEventRef"/>
      <xs:element name="transport" type="tns:transport"/>
      <xs:element name="transportSegmentDetails" type="tns:transportSegmentDetails"/>
      <xs:element name="walkSegmentDetails" type="tns:walkSegmentDetails"/>
      <xs:complexType name="getStatus">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="commands" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStatusResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getServicePatterns">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element minOccurs="0" name="lineId" type="xs:string"/>
          <xs:element minOccurs="0" name="directionId" type="xs:string"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getServicePatternsResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:servicePatternsResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="servicePatternsResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="servicePatterns" type="tns:servicePatternDetails"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="servicePatternDetails">
        <xs:sequence>
          <xs:element ref="tns:line"/>
          <xs:element name="direction" type="tns:pairIdName"/>
          <xs:element maxOccurs="unbounded" name="stopPoints" type="tns:stopPoint"/>
          <xs:element maxOccurs="unbounded" name="servicePatternNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="line">
        <xs:sequence>
          <xs:element ref="tns:transport"/>
          <xs:element name="groupOfLines" type="tns:pairIdName"/>
          <xs:element maxOccurs="unbounded" name="directions" type="tns:direction"/>
          <xs:element maxOccurs="unbounded" name="lineNotes" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="flexibleLineNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="code" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="accessibility" type="xs:string" use="required"/>
        <xs:attribute name="flexibleType" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="transport">
        <xs:sequence/>
        <xs:attribute name="mode" type="xs:string" use="required"/>
        <xs:attribute name="subMode" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="pairIdName">
        <xs:sequence/>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="direction">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="notes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="stopPoint">
        <xs:sequence>
          <xs:element minOccurs="0" ref="tns:city"/>
          <xs:element maxOccurs="unbounded" name="stopPointNotes" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="stopPointInDirectionNotes" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="lines" type="tns:line"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="latitude" type="xs:double" use="required"/>
        <xs:attribute name="longitude" type="xs:double" use="required"/>
        <xs:attribute name="accessibility" type="xs:string" use="required"/>
        <xs:attribute name="spijpStopInStation" type="xs:boolean" use="required"/>
        <xs:attribute name="spijpForBoarding" type="xs:boolean" use="required"/>
        <xs:attribute name="spijpForAlighting" type="xs:boolean" use="required"/>
      </xs:complexType>
      <xs:complexType name="city">
        <xs:sequence/>
        <xs:attribute name="inseeCode" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="notice">
        <xs:simpleContent>
          <xs:extension base="xs:string">
            <xs:attribute name="id" type="xs:string" use="required"/>
          </xs:extension>
        </xs:simpleContent>
      </xs:complexType>
      <xs:complexType name="getItinerary">
        <xs:sequence>
          <xs:element name="user" type="xs:string"/>
          <xs:element name="startPoint" type="tns:riInput"/>
          <xs:element name="endPoint" type="tns:riInput"/>
          <xs:element name="time" type="xs:dateTime"/>
          <xs:element name="startFrom" type="xs:boolean"/>
          <xs:element name="withTrafficEvents" type="xs:boolean"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="prefNetworks" type="xs:string"/>
          <xs:element name="prefJourney" type="xs:string"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="exclusionLines" type="xs:string"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="exclusionStops" type="xs:string"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="inclusionLines" type="xs:string"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="inclusionStops" type="xs:string"/>
          <xs:element name="withMobility" type="xs:boolean"/>
          <xs:element name="withDetails" type="xs:boolean"/>
          <xs:element minOccurs="0" name="applyFileForScoring" type="xs:boolean"/>
          <xs:element minOccurs="0" name="withEcoComparator" type="xs:boolean"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="riInput">
        <xs:sequence/>
        <xs:attribute name="type" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:string"/>
        <xs:attribute name="latitude" type="xs:double" use="required"/>
        <xs:attribute name="longitude" type="xs:double" use="required"/>
      </xs:complexType>
      <xs:complexType name="getItineraryResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:itineraryResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="itineraryResultat">
        <xs:sequence>
          <xs:element name="currentTime" type="xs:dateTime"/>
          <xs:element maxOccurs="unbounded" name="itineraries" type="tns:riItinerary"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="riItinerary">
        <xs:sequence>
          <xs:element name="type" type="tns:itineraryType"/>
          <xs:element name="startTime" type="xs:dateTime"/>
          <xs:element name="endTime" type="xs:dateTime"/>
          <xs:element name="duration" type="xs:int"/>
          <xs:element name="connectionNumber" type="xs:int"/>
          <xs:element name="impactPerburbation" type="tns:impactPerturbationType"/>
          <xs:element name="accessibility" type="xs:string"/>
          <xs:element minOccurs="0" ref="tns:ecoComparator"/>
          <xs:element maxOccurs="unbounded" name="trafficEvents" type="tns:situation"/>
          <xs:element maxOccurs="unbounded" name="itinerarySegments" type="tns:segment"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="ecoComparator">
        <xs:sequence>
          <xs:element name="distance" type="xs:double"/>
          <xs:element name="transportEmissions" type="xs:double"/>
          <xs:element name="personalCarEmissions" type="xs:double"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="situation">
        <xs:sequence>
          <xs:element name="id" type="xs:string"/>
          <xs:element name="version" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="validityPeriod" type="tns:pairDate"/>
          <xs:element name="publicationPeriod" type="tns:pairDate"/>
          <xs:element name="reason" type="xs:string"/>
          <xs:element name="subReason" type="xs:string"/>
          <xs:element ref="tns:affectScope"/>
          <xs:element maxOccurs="unbounded" name="infoMessages" type="tns:infoMessage"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="pairDate">
        <xs:sequence/>
        <xs:attribute name="startDate" type="xs:dateTime" use="required"/>
        <xs:attribute name="endDate" type="xs:dateTime" use="required"/>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="affectScope">
        <xs:sequence>
          <xs:element name="id" type="xs:string"/>
          <xs:element name="groupOfLines" type="tns:pairIdName"/>
          <xs:element maxOccurs="unbounded" name="lines" type="tns:affectedLine"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="affectedLine">
        <xs:sequence>
          <xs:element name="impact" type="tns:perturbationImpact"/>
          <xs:element maxOccurs="unbounded" name="stopPoints" type="tns:pairIdName"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="code" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="infoMessage">
        <xs:sequence>
          <xs:element name="shortContent" type="xs:string"/>
          <xs:element name="longContent" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="infoChannelCode" type="xs:string" use="required"/>
        <xs:attribute name="title" type="xs:string" use="required"/>
        <xs:attribute name="versionContent" type="xs:string" use="required"/>
        <xs:attribute name="creationTime" type="xs:dateTime" use="required"/>
        <xs:attribute name="contentModificationTime" type="xs:dateTime" use="required"/>
      </xs:complexType>
      <xs:complexType name="segment">
        <xs:sequence>
          <xs:element name="startTime" type="xs:dateTime"/>
          <xs:element name="endTime" type="xs:dateTime"/>
          <xs:element name="duration" type="xs:int"/>
          <xs:element ref="tns:transport"/>
          <xs:element name="impactPerburbation" type="tns:impactPerturbationType"/>
          <xs:element maxOccurs="unbounded" name="trafficEventsRefs" type="tns:trafficEventRef"/>
          <xs:element minOccurs="0" name="details" type="tns:segmentDetails"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="trafficEventRef">
        <xs:sequence/>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="impactPerburbation" type="tns:impactPerturbationType" use="required"/>
      </xs:complexType>
      <xs:complexType abstract="true" name="segmentDetails">
        <xs:sequence/>
      </xs:complexType>
      <xs:complexType name="transportSegmentDetails">
        <xs:complexContent>
          <xs:extension base="tns:segmentDetails">
            <xs:sequence>
              <xs:element ref="tns:line"/>
              <xs:element ref="tns:direction"/>
              <xs:element name="destination" type="tns:pairIdName"/>
              <xs:element name="lastCallForServiceLinkWithLine" type="xs:boolean"/>
              <xs:element ref="tns:servicePattern"/>
              <xs:element ref="tns:serviceJourney"/>
              <xs:element maxOccurs="unbounded" name="points" type="tns:riGeoPoint"/>
              <xs:element minOccurs="0" ref="tns:ecoComparator"/>
            </xs:sequence>
          </xs:extension>
        </xs:complexContent>
      </xs:complexType>
      <xs:complexType name="servicePattern">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="servicePatternNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="serviceJourney">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="serviceJourneyNotes" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="flexibleServiceNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="flexibleType" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="riGeoPoint">
        <xs:sequence>
          <xs:element minOccurs="0" ref="tns:city"/>
          <xs:element maxOccurs="unbounded" name="callPointNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="type" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="accessibility" type="xs:string" use="required"/>
        <xs:attribute name="latitude" type="xs:double" use="required"/>
        <xs:attribute name="longitude" type="xs:double" use="required"/>
        <xs:attribute name="stopInStation" type="xs:boolean" use="required"/>
        <xs:attribute name="schedule" type="xs:dateTime" use="required"/>
        <xs:attribute name="zone" type="xs:string"/>
      </xs:complexType>
      <xs:complexType name="walkSegmentDetails">
        <xs:complexContent>
          <xs:extension base="tns:segmentDetails">
            <xs:sequence>
              <xs:element name="startPoint" type="tns:riGeoPoint"/>
              <xs:element name="endPoint" type="tns:riGeoPoint"/>
              <xs:element minOccurs="0" ref="tns:ecoComparator"/>
            </xs:sequence>
          </xs:extension>
        </xs:complexContent>
      </xs:complexType>
      <xs:complexType name="getStopPoints">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element name="sortAlpha" type="xs:boolean"/>
          <xs:element minOccurs="0" name="groupOfLinesId" type="xs:string"/>
          <xs:element minOccurs="0" name="lineId" type="xs:string"/>
          <xs:element minOccurs="0" name="directionId" type="xs:string"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
          <xs:element minOccurs="0" name="stopPlaceId" type="xs:string"/>
          <xs:element minOccurs="0" name="fromCity" type="xs:string"/>
          <xs:element minOccurs="0" name="toCity" type="xs:string"/>
          <xs:element minOccurs="0" name="geoPoint" type="tns:searchGeoPoint"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="searchGeoPoint">
        <xs:sequence>
          <xs:element name="latitude" type="xs:double"/>
          <xs:element name="longitude" type="xs:double"/>
          <xs:element name="radius" type="xs:double"/>
          <xs:element name="deltaLon" type="xs:double"/>
          <xs:element name="deltaLat" type="xs:double"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStopPointsResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:stopPointsResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="stopPointsResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="stopPoints" type="tns:stopPoint"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getGroupOfLines">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getGroupOfLinesResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:groupOfLinesResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="groupOfLinesResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="groupsOfLines" type="tns:pairIdName"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="resolveIds">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="typeEntityIds" type="tns:objectId"/>
          <xs:element maxOccurs="unbounded" minOccurs="0" name="typeIds" type="tns:objectId"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="objectId">
        <xs:sequence/>
        <xs:attribute name="type" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="entityId" type="xs:string" use="required"/>
      </xs:complexType>
      <xs:complexType name="resolveIdsResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:resolveIdsResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="resolveIdsResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="objects" type="tns:objectId"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getOperators">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getOperatorsResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:operatorsResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="operatorsResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="operators" type="tns:pairIdName"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getLines">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element minOccurs="0" name="operatorId" type="xs:string"/>
          <xs:element minOccurs="0" name="groupOfLinesId" type="xs:string"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getLinesResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:linesResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="linesResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="lines" type="tns:line"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStops">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element name="maxResults" type="xs:int"/>
          <xs:element minOccurs="0" name="stopPlaceId" type="xs:string"/>
          <xs:element minOccurs="0" name="stopPointId" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="lineId" type="xs:string"/>
          <xs:element minOccurs="0" name="directionId" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStopsResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:stopsResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="stopsResultat">
        <xs:sequence>
          <xs:element name="currentTime" type="xs:dateTime"/>
          <xs:element maxOccurs="unbounded" name="stopsOnLines" type="tns:stopsOnLine"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="stopsOnLine">
        <xs:sequence>
          <xs:element ref="tns:line"/>
          <xs:element name="stopPoint" type="tns:pairIdName"/>
          <xs:element name="accessibility" type="xs:string"/>
          <xs:element maxOccurs="unbounded" name="stops" type="tns:stop"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="stop">
        <xs:sequence>
          <xs:element ref="tns:direction"/>
          <xs:element name="destination" type="tns:pairIdName"/>
          <xs:element name="servicePattern" type="tns:pairIdName"/>
          <xs:element name="stopInStation" type="xs:boolean"/>
          <xs:element name="startTime" type="xs:dateTime"/>
          <xs:element name="stopTime" type="xs:dateTime"/>
          <xs:element ref="tns:serviceJourney"/>
          <xs:element maxOccurs="unbounded" name="callPointNotes" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStopPlaces">
        <xs:sequence>
          <xs:element name="date" type="xs:dateTime"/>
          <xs:element name="sortAlpha" type="xs:boolean"/>
          <xs:element minOccurs="0" name="groupOfLinesId" type="xs:string"/>
          <xs:element minOccurs="0" name="lineId" type="xs:string"/>
          <xs:element minOccurs="0" name="id" type="xs:string"/>
          <xs:element minOccurs="0" name="name" type="xs:string"/>
          <xs:element minOccurs="0" name="stopPointId" type="xs:string"/>
          <xs:element minOccurs="0" name="geoPoint" type="tns:searchGeoPoint"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getStopPlacesResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:stopPlacesResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="stopPlacesResultat">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="stopPlaces" type="tns:stopPlace"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="stopPlace">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="lines" type="tns:line"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="latitude" type="xs:double" use="required"/>
        <xs:attribute name="longitude" type="xs:double" use="required"/>
      </xs:complexType>
      <xs:complexType name="getLineTimeTables">
        <xs:sequence>
          <xs:element name="startDate" type="xs:dateTime"/>
          <xs:element name="endDate" type="xs:dateTime"/>
          <xs:element name="maxResults" type="xs:int"/>
          <xs:element maxOccurs="unbounded" name="lineId" type="xs:string"/>
          <xs:element minOccurs="0" name="directionId" type="xs:string"/>
          <xs:element name="offsetStartDate" type="xs:int"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="getLineTimeTablesResponse">
        <xs:sequence>
          <xs:element minOccurs="0" name="return" type="tns:lineTimeTablesResultat"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="lineTimeTablesResultat">
        <xs:sequence>
          <xs:element name="currentTime" type="xs:dateTime"/>
          <xs:element maxOccurs="unbounded" name="lineTimeTables" type="tns:lineTimeTable"/>
          <xs:element maxOccurs="unbounded" name="notes" type="tns:notice"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="lineTimeTable">
        <xs:sequence>
          <xs:element ref="tns:line"/>
          <xs:element ref="tns:direction"/>
          <xs:element maxOccurs="unbounded" name="lineJourneys" type="tns:lineJourney"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="lineJourney">
        <xs:sequence>
          <xs:element minOccurs="0" ref="tns:servicePattern"/>
          <xs:element name="destination" type="tns:pairIdName"/>
          <xs:element ref="tns:serviceJourney"/>
          <xs:element maxOccurs="unbounded" name="callPoints" type="tns:callPoint"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType final="extension restriction" name="callPoint">
        <xs:sequence>
          <xs:element minOccurs="0" ref="tns:city"/>
          <xs:element maxOccurs="unbounded" name="callPointNotes" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="startTime" type="xs:dateTime" use="required"/>
        <xs:attribute name="stopTime" type="xs:dateTime" use="required"/>
        <xs:attribute name="accessibility" type="xs:string" use="required"/>
        <xs:attribute name="latitude" type="xs:double" use="required"/>
        <xs:attribute name="longitude" type="xs:double" use="required"/>
      </xs:complexType>
      <xs:complexType name="setPerturbations">
        <xs:sequence>
          <xs:element maxOccurs="unbounded" name="perts" type="tns:situation"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="setPerturbationsResponse">
        <xs:sequence>
          <xs:element name="return" type="xs:boolean"/>
        </xs:sequence>
      </xs:complexType>
      <xs:simpleType name="itineraryType">
        <xs:restriction base="xs:string">
          <xs:enumeration value="REGULAR"/>
          <xs:enumeration value="ADVISABLE"/>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType name="impactPerturbationType">
        <xs:restriction base="xs:string">
          <xs:enumeration value="normal"/>
          <xs:enumeration value="information"/>
          <xs:enumeration value="alert"/>
          <xs:enumeration value="critical"/>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType name="perturbationImpact">
        <xs:restriction base="xs:string">
          <xs:enumeration value="information"/>
          <xs:enumeration value="access_closed"/>
          <xs:enumeration value="link_closed"/>
          <xs:enumeration value="station_closed"/>
          <xs:enumeration value="trafic_slow"/>
          <xs:enumeration value="trafic_stopped"/>
          <xs:enumeration value="path_closed"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:schema>
  </wsdl:types>
  <wsdl:message name="resolveIdsResponse">
    <wsdl:part name="parameters" element="tns:resolveIdsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getGroupOfLinesResponse">
    <wsdl:part name="parameters" element="tns:getGroupOfLinesResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="resolveIds">
    <wsdl:part name="parameters" element="tns:resolveIds"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getLines">
    <wsdl:part name="parameters" element="tns:getLines"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="setPerturbationsResponse">
    <wsdl:part name="parameters" element="tns:setPerturbationsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getItineraryResponse">
    <wsdl:part name="parameters" element="tns:getItineraryResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStopPoints">
    <wsdl:part name="parameters" element="tns:getStopPoints"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStopPointsResponse">
    <wsdl:part name="parameters" element="tns:getStopPointsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStopPlacesResponse">
    <wsdl:part name="parameters" element="tns:getStopPlacesResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStopPlaces">
    <wsdl:part name="parameters" element="tns:getStopPlaces"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getServicePatternsResponse">
    <wsdl:part name="parameters" element="tns:getServicePatternsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getGroupOfLines">
    <wsdl:part name="parameters" element="tns:getGroupOfLines"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStatus">
    <wsdl:part name="parameters" element="tns:getStatus"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getOperators">
    <wsdl:part name="parameters" element="tns:getOperators"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStatusResponse">
    <wsdl:part name="parameters" element="tns:getStatusResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="setPerturbations">
    <wsdl:part name="parameters" element="tns:setPerturbations"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getLineTimeTablesResponse">
    <wsdl:part name="parameters" element="tns:getLineTimeTablesResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getLineTimeTables">
    <wsdl:part name="parameters" element="tns:getLineTimeTables"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStops">
    <wsdl:part name="parameters" element="tns:getStops"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getStopsResponse">
    <wsdl:part name="parameters" element="tns:getStopsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getOperatorsResponse">
    <wsdl:part name="parameters" element="tns:getOperatorsResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getItinerary">
    <wsdl:part name="parameters" element="tns:getItinerary"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getLinesResponse">
    <wsdl:part name="parameters" element="tns:getLinesResponse"></wsdl:part>
  </wsdl:message>
  <wsdl:message name="getServicePatterns">
    <wsdl:part name="parameters" element="tns:getServicePatterns"></wsdl:part>
  </wsdl:message>
  <wsdl:portType name="SmartMove">
    <wsdl:operation name="getStatus">
      <wsdl:input name="getStatus" message="tns:getStatus"></wsdl:input>
      <wsdl:output name="getStatusResponse" message="tns:getStatusResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getServicePatterns">
      <wsdl:input name="getServicePatterns" message="tns:getServicePatterns"></wsdl:input>
      <wsdl:output name="getServicePatternsResponse" message="tns:getServicePatternsResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getItinerary">
      <wsdl:input name="getItinerary" message="tns:getItinerary"></wsdl:input>
      <wsdl:output name="getItineraryResponse" message="tns:getItineraryResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStopPoints">
      <wsdl:input name="getStopPoints" message="tns:getStopPoints"></wsdl:input>
      <wsdl:output name="getStopPointsResponse" message="tns:getStopPointsResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getGroupOfLines">
      <wsdl:input name="getGroupOfLines" message="tns:getGroupOfLines"></wsdl:input>
      <wsdl:output name="getGroupOfLinesResponse" message="tns:getGroupOfLinesResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="resolveIds">
      <wsdl:input name="resolveIds" message="tns:resolveIds"></wsdl:input>
      <wsdl:output name="resolveIdsResponse" message="tns:resolveIdsResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getOperators">
      <wsdl:input name="getOperators" message="tns:getOperators"></wsdl:input>
      <wsdl:output name="getOperatorsResponse" message="tns:getOperatorsResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getLines">
      <wsdl:input name="getLines" message="tns:getLines"></wsdl:input>
      <wsdl:output name="getLinesResponse" message="tns:getLinesResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStops">
      <wsdl:input name="getStops" message="tns:getStops"></wsdl:input>
      <wsdl:output name="getStopsResponse" message="tns:getStopsResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStopPlaces">
      <wsdl:input name="getStopPlaces" message="tns:getStopPlaces"></wsdl:input>
      <wsdl:output name="getStopPlacesResponse" message="tns:getStopPlacesResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getLineTimeTables">
      <wsdl:input name="getLineTimeTables" message="tns:getLineTimeTables"></wsdl:input>
      <wsdl:output name="getLineTimeTablesResponse" message="tns:getLineTimeTablesResponse"></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="setPerturbations">
      <wsdl:input name="setPerturbations" message="tns:setPerturbations"></wsdl:input>
      <wsdl:output name="setPerturbationsResponse" message="tns:setPerturbationsResponse"></wsdl:output>
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="SmartMoveServiceSoapBinding" type="tns:SmartMove">
    <soap12:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="getStatus">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getStatus">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getStatusResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getServicePatterns">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getServicePatterns">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getServicePatternsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getItinerary">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getItinerary">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getItineraryResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getGroupOfLines">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getGroupOfLines">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getGroupOfLinesResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStopPoints">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getStopPoints">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getStopPointsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="resolveIds">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="resolveIds">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="resolveIdsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getOperators">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getOperators">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getOperatorsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getLines">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getLines">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getLinesResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStops">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getStops">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getStopsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getLineTimeTables">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getLineTimeTables">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getLineTimeTablesResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getStopPlaces">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="getStopPlaces">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getStopPlacesResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="setPerturbations">
      <soap12:operation soapAction="" style="document"/>
      <wsdl:input name="setPerturbations">
        <soap12:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="setPerturbationsResponse">
        <soap12:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="SmartMoveService">
    <wsdl:port name="SmartMovePort" binding="tns:SmartMoveServiceSoapBinding">
      <soap12:address location="http://localhost:9090/SmartMovePort"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>]]>
				</con:content>
				<con:type>http://schemas.xmlsoap.org/wsdl/</con:type>
			</con:part>
		</con:definitionCache>
		<con:endpoints>
			<con:endpoint>http://localhost:9090/SmartMovePort</con:endpoint>
		</con:endpoints>
		<con:operation id="{uuid3}" isOneWay="false" action="" name="getItinerary" bindingOperationName="getItinerary" type="Request-Response" outputName="getItineraryResponse" inputName="getItinerary" receivesAttachments="false" sendsAttachments="false">
			<con:settings/>
		</con:operation>
		
	</con:interface>
 """

BottomGlobal="""	<con:properties/>
	<con:wssContainer/>
	<con:oAuth2ProfileContainer/>
</con:soapui-project>
"""

testSuiteHead = """	
	<con:testSuite id="{uuid1}" name="{TestSuiteName}">
		<con:settings/>
		<con:runType>SEQUENTIAL</con:runType>
"""
testCaseHead = """        
		<con:testCase id="{uuid2}" failOnError="false" failTestCaseOnErrors="true" keepSession="false" maxResults="0" name="{TestSuiteName}" searchProperties="true">
			<con:settings/>
"""

testCaseBottom = """		
		</con:testCase>
        """
testSuiteBottom = """
		<con:properties/>
	</con:testSuite>
"""
	
	

			
		
testStepHead="""			<con:testStep type="request" name="{prefix} {numTest:03d} - {testName}" id="{uuid1}">
				<con:settings/>
				<con:config xsi:type="con:RequestStep" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
					<con:interface>SmartMoveServiceSoapBinding</con:interface>
					<con:operation>getItinerary</con:operation>
					<con:request name="RI num : {numTest} - {testName}" id="{uuid2}">
						<con:settings/>
						<con:encoding>UTF-8</con:encoding>
						<con:endpoint>{urlRvb}</con:endpoint>

"""
						
testStepBottom="""
						<con:assertion type="SOAP Response" id="{uuid1}"/>
						<con:assertion type="SOAP Fault Assertion" id="{uuid2}"/>
						<con:credentials>
							<con:authType>No Authorization</con:authType>
						</con:credentials>
						<con:jmsConfig JMSDeliveryMode="PERSISTENT"/>
						<con:jmsPropertyConfig/>
						<con:wsaConfig mustUnderstand="NONE" version="200508"/>
						<con:wsrmConfig version="1.2"/>
					</con:request>
				</con:config>
			</con:testStep>
"""


