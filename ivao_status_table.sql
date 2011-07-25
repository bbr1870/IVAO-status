BEGIN TRANSACTION;
DROP TABLE IF EXISTS status_ivao;
CREATE TABLE IF NOT EXISTS status_ivao (adminrating NUMERIC, altitude NUMERIC, atc_or_pilotrating NUMERIC, atis_message TEXT, callsign TEXT, client_software_name TEXT, client_software_version TEXT, clienttype TEXT, facilitytype TEXT, frequency NUMERIC, groundspeed NUMERIC, latitude NUMERIC, longitude NUMERIC, onground TEXT, planned_actdeptime NUMERIC, planned_aircraft TEXT, planned_altairport TEXT, planned_altairport2 TEXT, planned_altitude NUMERIC, planned_depairport TEXT, planned_depairport_lat TEXT, planned_depairport_lon TEXT, planned_deptime NUMERIC, planned_destairport TEXT, planned_destairport_lat NUMERIC, planned_destairport_lon NUMERIC, planned_flighttype TEXT, planned_hrsenroute NUMERIC, planned_hrsfuel NUMERIC, planned_minenroute NUMERIC, planned_minfuel NUMERIC, planned_pob TEXT, planned_remarks TEXT, planned_revision TEXT, planned_route TEXT, planned_tascruise NUMERIC, planned_typeofflight TEXT, protrevision TEXT, rating TEXT, realname TEXT, server TEXT, time_connected NUMERIC, time_last_atis_received NUMERIC, transponder NUMERIC, true_heading NUMERIC, vid NUMERIC, visualrange TEXT);
COMMIT;
