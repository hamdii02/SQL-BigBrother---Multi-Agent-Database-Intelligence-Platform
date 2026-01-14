import ReactMarkdown from "react-markdown";
import rehypePrism from "rehype-prism-plus";
// import '../../prism-custom.css';
import "prismjs/themes/prism-tomorrow.css";
import { memo } from "react";

const MemoizedMarkdown = memo(({ content }) => (
	<ReactMarkdown rehypePlugins={[rehypePrism]} children={content} />
  ));

const Markdown = ({ content }) => {
	return <MemoizedMarkdown content={content} />;
};

export default Markdown;
