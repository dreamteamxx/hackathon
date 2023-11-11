import { configureStore } from "@reduxjs/toolkit";
import { reducer as responsiveReducer } from "react-responsive-redux"
import userTypeSlice from "./slices/userTypeSlice.ts";
import userNameSlice from "./slices/userNameSlice.ts";

const store =  configureStore({
    reducer: {
        responsive: responsiveReducer,
        userType: userTypeSlice,
        userName: userNameSlice
    },
    devTools: true
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

export function clearStore() {
    store.dispatch({type: "RESET"})
}
export default store