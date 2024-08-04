const ErrorMessage = ({items}) => {
    return (items.length === 0 ? <h3>No Food Items</h3>: null);
}

export default ErrorMessage;