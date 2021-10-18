package com.finance.data.entity;

import lombok.*;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.Date;

@Entity @Table(name = "korea_stock")
@NoArgsConstructor @AllArgsConstructor
@Builder @Setter @Getter @ToString
public class KoreaStock {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "korea_stock_seq")
    private long koreaStockSeq;

    @Column(name = "stock_code")
    private String stockCode;

    @Column(name = "stock_price")
    private double stockPrice;

    @Column(name = "standard_date")
    private Date standardDate;

    @Column(name = "update_date")
    private Date updateDate;

    @NotBlank
    @Column(name = "from_data")
    private String fromData;

    @NotNull
    @Transient
    private long timestamp;
}
