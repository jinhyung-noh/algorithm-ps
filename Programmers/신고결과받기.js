function solution(idList, report, k) {
    
  const targetList = {}
  for (let i=0; i<report.length; i++){    
      const [reporter, reportee] = report[i].split(' ');
      if(targetList[reportee]) {
          if (targetList[reportee].indexOf(reporter) !== -1){
              continue;
          }
          targetList[reportee] = [...targetList[reportee], reporter];
      } else {
          targetList[reportee] = [reporter];
      }
  }
  // targetList complete: {reportee: reporter[]}
  const mailSending = {};
  const reportees = Object.keys(targetList);
  
  for (let i=0; i<reportees.length; i++){
      const reportee = reportees[i];
      const reporters = targetList[reportee];
      if (reporters.length < k){
          continue
      }

      for (let j=0; j<reporters.length; j++){
          const reporter = reporters[j];
          if (mailSending[reporter]){
              mailSending[reporter] += 1   
          } else {
              mailSending[reporter] = 1
          }
      }
  }
  
  const result = [];
  for (let i=0; i<idList.length; i++){
      const user = idList[i];
      if (mailSending[user]){
          result.push(mailSending[user]);
      } else {
          result.push(0);
      }
  }
  return result;
}