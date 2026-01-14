import moment from 'moment';

function formatTimestamp(timestamp) {
    // Kiểm tra tính hợp lệ của timestamp
    const date = new Date(timestamp);
    if (isNaN(date.getTime())) {
        return "";
    }

    const now = new Date();

    const sameDay = now.toDateString() === date.toDateString();

    const options = { hour: "numeric", minute: "numeric", hour12: true };
    const timeString = new Intl.DateTimeFormat("en-US", options).format(date);

    if (sameDay) {
        return timeString;
    } else {
        const diffTime = Math.abs(now - date);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return diffDays > 1
            ? `${timeString} - ${diffDays} days ago`
            : `${timeString} - yesterday`;
    }
}

function isNumber(str) {
    return typeof(str) == 'number';
}

function isDate(str) {
    return ("" + str).includes('GMT') || moment(str, moment.ISO_8601, true).isValid();
}

// console.log(isNumber("85000.00"))

function ArraysToMap(columns, rows){
    const result = []
    rows.forEach((row, i) => {
        const temp = {};
        row.forEach((cell, j) => {
            if(isDate(cell)) {
                temp[columns[j]] = new Date(cell).toLocaleDateString();
            }
            else {
                temp[columns[j]] = cell;
            }
        })
        result.push(temp)
    })

    return result;
} 


// const columns = ['OrderID', 'FirstName', 'ProductName', 'Total', 'OrderDate', 'Status'];
// const rows = [
//     [5, 'Charlie', 'Tent', '89.99', 'Mon, 19 Jun 2023 11:30:00 GMT', 'Shipped'],
//     [5, 'Charlie', 'Laptop', '1199.99', 'Mon, 19 Jun 2023 11:30:00 GMT', 'Shipped'],
//     [5, 'Charlie', 'T-shirt', '24.99', 'Mon, 19 Jun 2023 11:30:00 GMT', 'Shipped'],
//     [5, 'Charlie', 'Tablet', '499.99', 'Mon, 19 Jun 2023 11:30:00 GMT', 'Shipped'],
//     [4, 'Bob', 'Soccer Ball', '51.98', 'Sun, 18 Jun 2023 16:20:00 GMT', 'Cancelled'],
//     [3, 'Alice', 'Blender', '49.99', 'Sat, 17 Jun 2023 12:00:00 GMT', 'Delivered'],
//     [3, 'Alice', 'Jeans', '15.99', 'Sat, 17 Jun 2023 12:00:00 GMT', 'Delivered'],
//     [2, 'Jane', 'Novel', '19.99', 'Fri, 16 Jun 2023 09:45:00 GMT', 'Processing'],
//     [1, 'John', 'Smartphone', '699.99', 'Thu, 15 Jun 2023 14:30:00 GMT', 'Shipped'],
//     [1, 'John', 'Novel', '19.99', 'Thu, 15 Jun 2023 14:30:00 GMT', 'Shipped']
// ]

// const map = ArraysToMap(columns, rows);
// console.log(map)

export { formatTimestamp, ArraysToMap, isDate, isNumber };