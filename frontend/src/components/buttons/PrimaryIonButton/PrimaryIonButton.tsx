import {IonButton} from "@ionic/react";
import {ionButtonProperties} from "../../../interfaces/ionButtonInterface.ts";
import cl from "./primaryIonButton.module.css"

export default function primaryIonButton({disabled, routerLink, wrapperStyle, onClick,  id, style, routerDirection, rel, routerAnimation, target, children, expand, form, fill, mode, href, size, shape, type, strong, download}:ionButtonProperties){
    return(
        <div className={cl.primaryButton} style={wrapperStyle}>
            <IonButton disabled={disabled} routerLink={routerLink} id={id} style={style} onClick={onClick} routerDirection={routerDirection} rel={rel} routerAnimation={routerAnimation} target={target} expand={expand} form={form} fill={fill} mode={mode} href={href} size={size} shape={shape} type={type} strong={strong} download={download}>
                {children}
            </IonButton>
        </div>
    )
}