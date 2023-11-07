import {IonContent, IonHeader, IonTitle, IonToolbar} from "@ionic/react";
// import {useEffect, useRef, useState} from "react";
// import mapboxgl from "mapbox-gl"
export default function MapPage(){
    // const mapContainer = useRef(null)
    //     const map = useRef(null)
    //     const [lng, setLng] = useState(37.61556)
    //     const [lat, setLat] = useState(55.75222)
    //     const [zoom, setZoom] = useState(9)
    // useEffect(() => {
    //     if (map.current) return; // initialize map only once
    //     map.current = new mapboxgl.Map({
    //         container: mapContainer.current,
    //         style: 'mapbox://styles/mapbox/streets-v12',
    //         center: [lng, lat],
    //         zoom: zoom
    //     });
    // });
    return(
        <>
            <IonHeader mode={"md"}>
                <IonToolbar mode={"md"}>
                    <IonTitle>
                        <h1>Карта</h1>
                    </IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent fullscreen={true}>
                <div style={{
                    display: 'flex',
                    flexDirection: "column",
                    justifyContent: 'center',
                    minHeight: "100%"
                }}>
                    Карты нет и токена тоже 😥
                </div>
            </IonContent>
        </>
    )
}