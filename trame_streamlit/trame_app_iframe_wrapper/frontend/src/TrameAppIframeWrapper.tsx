import { TrameIframeApp } from "@kitware/trame-react";
import React, { useRef, useEffect } from "react";
import {
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";

type TrameAppIframeWrapperProps = {
  args: object;
};

const TrameAppIframeWrapper: React.FC<TrameAppIframeWrapperProps> = ({ args }) => {
  const communicator = useRef(null);
  const viewerId = args["viewer_id"];
  const trameAppUrl = args["trame_app_url"];

  useEffect(() => {
    Streamlit.setFrameHeight(500);

    if (communicator.current) {
      Streamlit.setComponentReady();
    }
  }, []);

  useEffect(() => {
    if (!communicator.current) {
      return;
    }
    const state = args["state"];
    console.debug("updating trame state - ", state);
    communicator.current.state.update(state);
  }, [args]);


  const onViewerReady = (comm) => {
    Streamlit.setComponentReady();

    const syncStateKeys = args["sync_state_keys"];
    communicator.current = comm;

    comm.state.onReady(() => {
      comm.state.watch(syncStateKeys, (...stateValues) => {
        const componentValue = {};
        // @ts-ignore 
        stateValues.entries().forEach(([idx, stateVal]) => {
          console.log(`${syncStateKeys[idx]} changed - new val: `, stateVal);
          componentValue[syncStateKeys[idx]] = stateVal;
        });
        Streamlit.setComponentValue(componentValue);
      });
    });
  };


  return (
    <TrameIframeApp
      style={{ height: "100%", width: "100%" }}
      iframeId={viewerId}
      url={trameAppUrl}
      onCommunicatorReady={onViewerReady}
      key={viewerId}
    />
  );
};

export default withStreamlitConnection(TrameAppIframeWrapper);
