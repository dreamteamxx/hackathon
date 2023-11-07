import {useEffect, useRef, useState} from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css"

export default function MapboxMap(){
    const mapContainer = useRef(null)
    const map = useRef(null)
    const [lng, setLng] = useState(37.61556)
    const [lat, setLat] = useState(55.75222)
    const [zoom, setZoom] = useState(9)
    const [mapboxMap, setMap] = useState<mapboxgl.Map>()
    useEffect(() => {
        if (typeof window === "undefined" || mapContainer.current === null) return;
        if (map.current) return; // initialize map only once
        // @ts-ignore
        const mapboxMap = new mapboxgl.Map({
            container: mapContainer.current,
            accessToken: "pk.eyJ1IjoiaHVtNG5vaWQiLCJhIjoiY2xva2hkcmxpMjd2NjJrbWU2MHRyOHVtdiJ9.UAu-FTRR-PHjGoQFZxV-Kg",
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [lng, lat],
            zoom: zoom
        });
        setMap(mapboxMap)

        return () => {
            mapboxMap.remove()
        }

    });
    return (
        <>
            <div style={{
                minWidth: "100%",
                maxWidth: "100%"
            }}>
                <div ref={mapContainer} style={{
                    width: "100%",
                    height: "100%"
                }} />
            </div>
        </>
    )
}