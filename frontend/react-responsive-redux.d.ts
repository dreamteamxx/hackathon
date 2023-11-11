declare module 'react-responsive-redux'{
    import React from "react";
    interface state {
        phone: boolean,
        tablet: boolean,
        mobile: boolean,
        desktop: boolean,
        fakeWidth: number
    }
    export const reducer: () => state

    export const MobileScreen: ({children}:{children:React.ReactNode}) => React.ReactNode

}