import Map from "react-map-gl"
import 'mapbox-gl/dist/mapbox-gl.css';

export default function MapboxMap(){
    return (
        <Map
            mapLib={import('mapbox-gl')}
            mapboxAccessToken={import.meta.env.VITE_MAPBOX_API_TOKEN}
            initialViewState={{
                longitude: -100,
                latitude: 40,
                zoom: 3.5
            }}
            style={{width: "100%", height: "100vh"}}
            mapStyle="mapbox://styles/mapbox/streets-v12"
        />
    )
}