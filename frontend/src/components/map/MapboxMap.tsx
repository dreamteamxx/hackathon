import Map, {GeolocateControl, useControl} from "react-map-gl"
import 'mapbox-gl/dist/mapbox-gl.css';
import {useRef} from "react";
import * as mapboxgl from "mapbox-gl";
import MapboxLanguage from "@mapbox/mapbox-gl-language";


export default function MapboxMap(){
    const geoControlRef = useRef<mapboxgl.GeolocateControl>(null)
    function LanguageControl() {
        useControl(() => new MapboxLanguage({defaultLanguage: "ru"}))
        return null
    }
    return (
        <Map
            mapLib={import('mapbox-gl')}
            mapboxAccessToken={import.meta.env.VITE_MAPBOX_API_TOKEN}
            initialViewState={{
                longitude: 37.61729990,
                latitude: 55.75582600,
                zoom: 3.5
            }}
            onLoad={() => {geoControlRef.current?.trigger()}}
            style={{width: "100%", height: "100vh"}}
            mapStyle="mapbox://styles/mapbox/streets-v11"

        >
            <GeolocateControl ref={geoControlRef}/>
            <LanguageControl/>
        </Map>
    )
}