// import {useRouteError} from "react-router-dom";

export default function Error() {
    // @ts-ignore
    // const error:{
    //     statusText?: string,
    //     message?: string
    // } = useRouteError()
    // console.error(error)

    return (
        <div id={"error-page"}>
            <h1>ОЙ</h1>
            <p>Что-то пошло не так</p>
            {/*<p>*/}
            {/*    <i>{error.statusText || error.message}</i>*/}
            {/*</p>*/}
        </div>
    )
}