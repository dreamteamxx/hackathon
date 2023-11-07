import React, {CSSProperties, MouseEventHandler} from "react";
import {AnimationBuilder} from "@ionic/react";

export interface ionButtonProperties {
    children?: React.ReactNode,
    disabled?: boolean,
    download?: string,
    expand?: 'block' | 'full' | undefined,
    fill?: 'clear' | 'default' | 'outline' | 'solid' | undefined,
    form?: HTMLFormElement | string | undefined,
    href?: string | undefined,
    mode?: 'ios' | 'md',
    rel?: string | undefined,
    routerAnimation?: AnimationBuilder | undefined,
    routerDirection?: "back" | "forward" | "root",
    routerLink?: string
    shape?: "round" | undefined,
    size?: "default" | "large" | "small" | undefined,
    strong?: boolean,
    target?: string | undefined,
    type?: 'button' | 'reset' | 'submit',
    id?: string,
    style?: CSSProperties,
    onClick?: MouseEventHandler<HTMLIonButtonElement>,
    wrapperStyle?: CSSProperties,
}