package com.finance.data.service;

import com.finance.data.entity.USStock;
import com.finance.data.repository.USStockRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Locale;

@Service
public class USStockService {

    @Autowired
    private USStockRepository usStockRepository;

    public USStock saveUSStock(USStock usStock) {
        USStock newUSStock = USStock.builder()
                .stockCode(usStock.getStockCode().toUpperCase(Locale.ROOT))
                .stockPrice(usStock.getStockPrice())
                .fromData(usStock.getFromData())
                .standardDate(new Date(usStock.getTimestamp()*1000L))
                .updateDate(new Date())
                .build();
        return usStockRepository.save(newUSStock);
    }
}
