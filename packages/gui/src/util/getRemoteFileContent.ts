export enum FileType {
  Binary = 'binary',
  Video = 'video',
  Image = 'image',
}

export type RemoteFileContent = {
  uri: string;
  maxSize?: number;
  forceCache?: boolean;
  nftId?: string;
  type?: FileType;
  dataHash?: string;
};

export default async function getRemoteFileContent(
  props: RemoteFileContent,
): Promise<{
  data: string;
  encoding: string;
}> {
  const ipcRenderer = (window as any).ipcRenderer;
  const requestOptions = {
    url: props.uri,
    maxSize: props.maxSize,
    forceCache: props.forceCache,
    nftId: props.nftId,
    type: props.type,
    dataHash: props.dataHash,
  };

  const { data, statusCode, encoding, error } = await ipcRenderer?.invoke(
    'fetchBinaryContent',
    requestOptions,
  );

  if (error) {
    throw error;
  }

  if (statusCode !== 200) {
    throw new Error(error?.message || `Failed to fetch content from ${url}`);
  }

  return { data, encoding };
}
