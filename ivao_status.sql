PRAGMA encoding = "UTF-8";
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS airlines;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cprefix;
DROP TABLE IF EXISTS fir;
DROP TABLE IF EXISTS firs;
DROP TABLE IF EXISTS friends;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS recent;
DROP TABLE IF EXISTS schedule_controllers;
DROP TABLE IF EXISTS schedule_pilots;
DROP TABLE IF EXISTS staff;

CREATE TABLE IF NOT EXISTS aircraft (icao TEXT, fabricant TEXT, model TEXT, code TEXT, category TEXT);
CREATE TABLE IF NOT EXISTS airlines (code TEXT, airline_name TEXT, callsign TEXT, reality TEXT);
CREATE TABLE IF NOT EXISTS airports (icao TEXT, airport TEXT, city TEXT, country TEXT, fir TEXT, latitude NUMERIC, longitude NUMERIC);
CREATE TABLE IF NOT EXISTS countries (id_country TEXT, country TEXT, icao TEXT, latitude NUMERIC, longitude NUMERIC);
CREATE TABLE IF NOT EXISTS cprefix (icao_initial TEXT, id_country);
CREATE TABLE IF NOT EXISTS fir (fir TEXT, latitude NUMERIC, longitude NUMERIC);
CREATE TABLE IF NOT EXISTS firs (fir TEXT, location TEXT, id_country, city TEXT, control_type TEXT, latitude NUMERIC, longitude NUMERIC, name TEXT);
CREATE TABLE IF NOT EXISTS friends (vid NUMERIC, realname TEXT, rating TEXT, clienttype TEXT);
CREATE TABLE IF NOT EXISTS ratings (id NUMERIC, controller_level TEXT, controller_rating TEXT, pilot_level TEXT, pilot_rating TEXT);
CREATE TABLE IF NOT EXISTS recent (adminrating NUMERIC, altitude NUMERIC, atc_or_pilotrating NUMERIC, atis_message TEXT, callsign TEXT, client_software_name TEXT, client_software_version TEXT, clienttype TEXT, facilitytype TEXT, frequency NUMERIC, groundspeed NUMERIC, latitude NUMERIC, longitude NUMERIC, onground TEXT, planned_actdeptime NUMERIC, planned_aircraft TEXT, planned_altairport TEXT, planned_altairport2 TEXT, planned_altitude NUMERIC, planned_depairport TEXT, planned_depairport_lat TEXT, planned_depairport_lon TEXT, planned_deptime NUMERIC, planned_destairport TEXT, planned_destairport_lat NUMERIC, planned_destairport_lon NUMERIC, planned_flighttype TEXT, planned_hrsenroute NUMERIC, planned_hrsfuel NUMERIC, planned_minenroute NUMERIC, planned_minfuel NUMERIC, planned_pob NUMERIC, planned_remarks TEXT, planned_revision TEXT, planned_route TEXT, planned_tascruise NUMERIC, planned_typeofflight TEXT, protrevision TEXT, rating TEXT, realname TEXT, server TEXT, time_connected NUMERIC, time_last_atis_received NUMERIC, transponder NUMERIC, true_heading NUMERIC, vid NUMERIC, visualrange TEXT);
CREATE TABLE IF NOT EXISTS schedule_controllers (name TEXT, position TEXT, StartDateUTC TEXT, EndDateUTC TEXT, voice TEXT, training TEXT, event TEXT);
CREATE TABLE IF NOT EXISTS schedule_pilots (name TEXT, voice TEXT, training TEXT, event TEXT, callsign TEXT, airplane TEXT, departure TEXT, DepTime TEXT, Destination TEXT, DestTime TEXT, altitude NUMERIC, CruisingSpeed NUMERIC, route TEXT);
CREATE TABLE IF NOT EXISTS staff (callsign TEXT, name TEXT, id1, id2, id3);

COMMIT;
