function AVG(bills) {
    if (bills.length==0){
        return 0
    }
    suma = 0;
    for (var i=0;i<bills.length;i++) {
        suma+=bills[i]
    }
    return suma/bills.length;
}

calculatorJohn = {
    bills: [124,48,268,180,42],
    calculate: function(){
        tips = [];
        totals = [];
        for (var i=0; i<this.bills.length; i++){
            if (this.bills[i] < 50) {
                tips.push(this.bills[i]*0.20);
                totals.push(this.bills[i]*1.20);
            } else if (this.bills[i]<=200) {
                tips.push(this.bills[i]*0.15);
                totals.push(this.bills[i]*1.15);
            } else {
                tips.push(this.bills[i]*0.1);
                totals.push(this.bills[i]*1.1);
            }            
        }
        return [tips, totals];
    }
}

calculatorMark = {
    bills: [77,375,110,45],
    calculate: function(){
        tips = [];
        totals = [];
        for (var i=0; i<this.bills.length; i++){
            if (this.bills[i] < 100) {
                tips.push(this.bills[i]*0.20);
                totals.push(this.bills[i]*1.20);
            } else if (this.bills[i]<=300) {
                tips.push(this.bills[i]*0.1);
                totals.push(this.bills[i]*1.1);
            } else {
                tips.push(this.bills[i]*0.25);
                totals.push(this.bills[i]*1.25);
            }            
        }
        return [tips, totals];
    }
}

//console.log(calculatorJohn.calculate())
//console.log(calculatorMark.calculate())
//console.log(AVG(calculatorJohn.calculate()[0]))
//console.log(AVG(calculatorMark.calculate()[0]))

if (AVG(calculatorMark.calculate()[0])>AVG(calculatorJohn.calculate()[0])) {
    console.log("Mark pagó más propina de media")
} else if (AVG(calculatorMark.calculate()[0])<AVG(calculatorJohn.calculate()[0])) {
    console.log("John pagó más propina de media")   
} else {
    console.log("Los dos pagaron igual propina de media")
}
